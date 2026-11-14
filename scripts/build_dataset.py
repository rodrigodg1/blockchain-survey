"""Rebuild or validate the retained dataset and comparisons.

Uses Python's standard library to validate source records, publication identities,
and generated outputs. Retrieval and screening are not repeated.
"""
from collections import Counter
from pathlib import Path
import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
import tempfile

from .source_tables import extract_membership, platform_records, plain_text

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_UPDATE_KEYS = {
    'updateMasood2024Patient', 'updateCan2024AuditableConsent',
    'updateJaved2024SecureConsent', 'updatePhuyal2026Architecture',
    'updateZeydan2024SSI', 'updateAgarkar2024BADIMAC',
    'updateMaZhang2024Rollup', 'updateDhasaratha2024IoMT',
}
MEMBERSHIP_SOURCE = 'revisao/collection-membership.json'
MATRIX_SOURCE = 'revisao/synthesis-evidence-matrix.csv'
APPLICATION_MATRIX_ROLES = {
    'historical_application', 'recent_application',
    'recent_application_addition', 'recent_application_search_completion',
    'recent_application_database_update', 'recent_application_protocol_followup',
}
QUERY_GROUPS = {f'S{i:02}': group for group, start in
                [('privacy', 1), ('consent', 4), ('identity', 7)]
                for i in range(start, start + 3)}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def csv_bytes(records, columns):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=columns, lineterminator='\n')
    writer.writeheader()
    writer.writerows(records)
    return stream.getvalue().encode('utf-8')


def load_snapshot(root):
    snapshot = json.loads((root / 'data/source-snapshot.json').read_text(encoding='utf-8'))
    for name, expected in snapshot['source_files'].items():
        if digest((root / 'data/sources' / name).read_bytes()) != expected:
            raise ValueError(f'Source differs from documented snapshot: {name}')
    return snapshot


def validate_source_membership(collection, matrix, recent, retained, snapshot, membership,
                                   inventory_text, derivations):
    if membership['reference_source_sha256'] != snapshot['reference_source_sha256']:
        raise ValueError('Reference source membership fingerprint differs from source snapshot')
    if membership['current_plot_files'] != snapshot['current_plot_files']:
        raise ValueError('Current plot membership differs from reference source snapshot')

    def unique_ids(values, description):
        if any(not isinstance(key, str) or not key.strip() for key in values):
            raise ValueError(f'Invalid identity in {description}')
        if len(values) != len(set(values)):
            raise ValueError(f'Duplicate identities in {description}')
        return set(values)

    works = membership['included_works']
    included_ids = unique_ids([r['study_id'] for r in works], 'reference source application membership')
    detailed_ids = unique_ids(membership['detailed_example_ids'], 'detailed application membership')
    contextual_ids = unique_ids(membership['contextual_source_ids'], 'contextual membership')
    privacy_evaluation_ids = unique_ids(membership['privacy_evaluation_ids'], 'privacy evaluation membership')
    collection_by_id = {r['study_id']: r for r in collection}
    if contextual_ids & (included_ids | detailed_ids | set(collection_by_id)):
        raise ValueError('Contextual sources cannot enter included or detailed application membership')
    if included_ids != set(collection_by_id):
        raise ValueError('Included application membership differs from reference source')
    for work in works:
        row = collection_by_id[work['study_id']]
        if (work['review_group'], work['source_table']) != (row['review_group'], row['source_table']):
            raise ValueError('Reference source group or table differs for study: ' + work['study_id'])
    if not detailed_ids <= included_ids:
        raise ValueError('Detailed examples must belong to the included application collection')

    matrix_ids = unique_ids([r['citation_key'] for r in matrix], 'synthesis matrix')
    matrix_applications, matrix_context = set(), set()
    for row in matrix:
        role = row['collection_role']
        if role in APPLICATION_MATRIX_ROLES:
            matrix_applications.add(row['citation_key'])
        elif role.startswith('context_'):
            matrix_context.add(row['citation_key'])
        else:
            raise ValueError('Unrecognized synthesis collection role: ' + role)
    if detailed_ids != matrix_applications:
        raise ValueError('Detailed application membership differs from synthesis matrix')
    if contextual_ids != matrix_context:
        raise ValueError('Contextual membership differs from synthesis matrix')
    if matrix_ids != detailed_ids | contextual_ids:
        raise ValueError('Synthesis matrix contains identities outside the declared membership')

    evaluation_counts = {}
    for group in ('privacy', 'consent', 'identity'):
        ids = unique_ids(membership['evaluation_ids_by_group'][group], group + ' evaluation membership')
        expected_ids = {r['citation_key'] for r in recent
                        if QUERY_GROUPS[retained[r['citation_key']]['query_id']] == group
                        and r['evaluation'].strip()}
        if ids != expected_ids or not ids <= detailed_ids:
            raise ValueError(group + ' evaluation membership differs from primary extraction')
        evaluation_counts[group] = len(ids)
    if privacy_evaluation_ids != set(membership['evaluation_ids_by_group']['privacy']):
        raise ValueError('Privacy evaluation membership fields disagree')
    if evaluation_counts != snapshot['counts']['evaluation_summaries_by_group']:
        raise ValueError('Evaluation counts disagree with reference source membership')

    # Plot inputs retain the exact six inventory tables without redistributing
    # the complete reference source. Detailed membership is checked against the matrix above.
    excerpt_works = []
    table_groups = {r['source_table']: r['review_group'] for r in works}
    for block in re.findall(r'\\begin\{longtable\}.*?\\end\{longtable\}', inventory_text, re.S):
        label = re.search(r'\\label\{([^}]+)\}', block)
        if not label or label[1] not in table_groups:
            raise ValueError('Unknown table in reference source inventory excerpt')
        for line in block.splitlines():
            if not line.startswith(r'\cite{'):
                continue
            key = re.match(r'\\cite\{([^}]+)\}', line)[1]
            excerpt_works.append({'study_id': key, 'review_group': table_groups[label[1]],
                                  'source_table': label[1]})
    if excerpt_works != works:
        raise ValueError('Reference source inventory excerpt differs from recorded membership')

    objectives = {f'G{i}' for i in range(1, 9)}
    matrix_by_id = {r['matrix_id']: r for r in matrix}
    if set(membership['research_questions']) != {'RQ1', 'RQ2', 'RQ3'}:
        raise ValueError('Reference source research questions are missing or duplicated')
    if {r['requirement_id'] for r in derivations} != objectives or len(derivations) != 8:
        raise ValueError('Missing or duplicate objective derivation')
    if set(membership['objective_source_ids']) != objectives:
        raise ValueError('Reference source objective citations are incomplete')
    for row in derivations:
        anchors = row['application_matrix_ids'].split(';')
        if len(set(anchors)) < 2:
            raise ValueError('Each objective requires its recorded application contrast')
        expected_keys = {matrix_by_id[a]['citation_key'] for a in anchors}
        if not expected_keys <= set(membership['objective_source_ids'][row['requirement_id']]):
            raise ValueError('Objective citations differ from reference source derivation')
        for anchor in anchors:
            source = matrix_by_id[anchor]
            if source['citation_key'] not in detailed_ids or source['verification_status'] != 'primary_fulltext_verified':
                raise ValueError('Objective anchor lacks its recorded direct primary-text check')

    expected = snapshot['counts']
    if (len(contextual_ids), len(privacy_evaluation_ids)) != (
            expected['contextual_sources'], expected['privacy_evaluation_summaries']):
        raise ValueError('Snapshot contextual/evaluation counts disagree with membership')

    return {
        'contextual_sources': len(contextual_ids),
        'privacy_evaluation_summaries': len(privacy_evaluation_ids),
        'evaluation_summaries_by_group': evaluation_counts,
        'contextual_sources_in_application_denominator': False,
    }


def build_artifacts(root=ROOT):
    root = Path(root)
    snapshot = load_snapshot(root)
    source_root = root / 'data/sources'
    for name in (MEMBERSHIP_SOURCE, MATRIX_SOURCE):
        if name not in snapshot['source_files']:
            raise ValueError('Required membership source is not fingerprinted in snapshot: ' + name)
    membership = json.loads((source_root / MEMBERSHIP_SOURCE).read_text(encoding='utf-8'))
    inventory_text = (source_root / 'revisao/application-inventory.tex').read_text(encoding='utf-8')
    comparison_text = (source_root / 'revisao/comparison-excerpts.tex').read_text(encoding='utf-8')
    DATE = snapshot['artifact_date']
    OUT = Path('.')
    artifacts = {}

    def rows(name):
        with (source_root / name).open(newline='', encoding='utf-8') as stream:
            return list(csv.DictReader(stream))

    def write_csv(path, records, columns=None):
        artifacts[path.name] = csv_bytes(records, columns or list(records[0]))

    bib = (source_root / 'references-revised.bib').read_text(encoding='utf-8')
    starts = list(re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib))
    blocks = {m[1]: bib[m.start():starts[i+1].start() if i+1 < len(starts) else len(bib)]
              for i, m in enumerate(starts)}

    def field(key, name):
        text = blocks[key]
        match = re.search(r'\b' + name + r'\s*=\s*', text, re.I)
        if not match:
            return ''
        start = match.end()
        if text[start] != '{':
            return text[start:].split(',')[0].strip('" \n')
        depth, end = 1, start + 1
        while depth:
            if text[end] == '{' and text[end-1] != '\\':
                depth += 1
            elif text[end] == '}' and text[end-1] != '\\':
                depth -= 1
            end += 1
        return text[start+1:end-1]

    def normal_doi(value):
        return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', value.strip(), flags=re.I).lower()

    historical = rows('historical-extraction.csv')
    recent = rows('revisao/recent-extraction.csv')
    scholar = rows('revisao/protocol-search-records.csv')
    scholar_retained = {r['citation_key']: r for r in scholar}
    if any(r['decision'] != 'retained_after_primary_text_check' for r in scholar):
        raise ValueError('Scholar records contain an unselected publication')
    if len(scholar_retained) != len(scholar) or '' in scholar_retained:
        raise ValueError('Duplicate or missing inclusion identity in Scholar records')
    retained = dict(scholar_retained)
    additional = []
    for record in rows('revisao/scopus-included-records.csv'):
        queries = json.loads(record['query_ids'])
        if (record['decision'] != 'retained_after_primary_text_check'
                or len({QUERY_GROUPS[q] for q in queries}) != 1
                or not record['primary_text_url']):
            raise ValueError('Scopus inclusion lacks an unambiguous query family or primary source')
        additional.append({'citation_key': record['current_citation_key'],
                           'query_id': queries[0], 'record_id': record['record_id']})
    followup = rows('revisao/protocol-followup-records-2026-10-26.csv')
    if any(r['decision'] != 'retained_after_primary_text_check' for r in followup):
        raise ValueError('Follow-up records contain an unselected publication')
    for record in additional + followup:
        key = record['citation_key']
        if not key or key in retained:
            raise ValueError('Duplicate or missing inclusion identity across retrieval strata')
        if 'review_group' in record and QUERY_GROUPS[record['query_id']] != record['review_group']:
            raise ValueError('Follow-up query family disagrees with recorded group')
        retained[key] = record
    query_groups = QUERY_GROUPS
    groups = ['privacy', 'consent', 'identity']
    collection = []

    for batch, records, source in [
        ('historical', historical, 'historical-extraction.csv'),
        ('supplementary_update', recent, 'revisao/recent-extraction.csv'),
    ]:
        for record_number, record in enumerate(records, 1):
            key = record['citation_key']
            native = retained.get(key, {}) if batch == 'supplementary_update' else {}
            is_old = batch == 'historical'
            doi = normal_doi(field(key, 'doi'))
            collection.append({
                'study_id': key,
                'collection': batch,
                'review_group': record['historical_group'] if is_old else query_groups[native['query_id']],
                'group_basis': 'original_extraction_group' if is_old else 'documented_retrieval_query_family',
                'title_bibtex': field(key, 'title'),
                'authors_bibtex': field(key, 'author'),
                'extraction_year': record['publication_year'] if is_old else record['year'],
                'bibliography_year': field(key, 'year'),
                'doi': doi,
                'publication_url': 'https://doi.org/' + doi if doi else field(key, 'url'),
                'application': record['use_case'] if is_old else record['application'],
                'reported_approach': record['reported_technique'] if is_old else record['approach'],
                'reported_contribution': record['reported_contribution'] if is_old else record['contribution'],
                'reported_platform': record['reported_platform'] if is_old else record['blockchain_platform'],
                'reported_software_link': record['reported_software_link'] if is_old else record['implementation_link'],
                'reported_evaluation': '' if is_old else record['evaluation'],
                'evidence_boundary': '' if is_old else record['boundary'],
                'primary_text_source_url': '' if is_old else record['source_url'],
                'primary_text_evidence_location': '' if is_old else record['evidence_location'],
                'query_id_observed': native.get('query_id', ''),
                'native_record': '' if is_old else record['native_record'],
                'source_table': record['source_table'] if is_old else (record.get('source_table') or ('tab:focused-update' if key in ORIGINAL_UPDATE_KEYS else 'tab:focused-update-additions')),
                'source_extraction_file': source,
                'source_record_number': record_number,
                'verification_scope': record['verification_scope'] if is_old else
                    'Primary text and publication identity checked for extracted descriptions; '
                    'author claims qualified; no independent reproduction or compliance certification',
            })

    if not (len(historical) == 98 and len(recent) == len(retained)):
        raise ValueError('Historical count or recent retained/extraction counts disagree')
    if not ORIGINAL_UPDATE_KEYS <= set(retained):
        raise ValueError('Original eight update studies must be retained')
    if not ({r['citation_key'] for r in recent} == set(retained)):
        raise ValueError("Invalid source data: {r['citation_key'] for r in recent} == set(retained)")
    if not (len(collection) == len({r['study_id'] for r in collection}) == len(historical) + len(recent)):
        raise ValueError('Collection contains duplicate identities or incorrect stratum totals')
    hc = Counter(r['historical_group'] for r in historical)
    uc = Counter(query_groups[r['query_id']] for r in retained.values())
    cc = Counter(r['review_group'] for r in collection)
    if not (hc == {'privacy': 40, 'consent': 33, 'identity': 25}):
        raise ValueError("Invalid source data: hc == {'privacy': 40, 'consent': 33, 'identity': 25}")
    if cc != hc + uc:
        raise ValueError('Combined accounting groups disagree with the two source strata')
    dois = [r['doi'] for r in collection if r['doi']]
    titles = [re.sub(r'[^a-z0-9]', '', r['title_bibtex'].lower()) for r in collection]
    if not (len(dois) == len(set(dois))):
        raise ValueError('Duplicate nonempty DOI in application collection')
    if not (len(titles) == len(set(titles))):
        raise ValueError('Duplicate normalized title in application collection')
    detailed_analysis = validate_source_membership(
        collection, rows(MATRIX_SOURCE), recent, retained, snapshot, membership,
        inventory_text, rows('revisao/requirement-derivation.csv'))

    extracted, _, summaries = extract_membership(
        (inventory_text + '\n\n' + comparison_text).encode('utf-8'),
        membership['evaluation_ids_by_group'])
    for key, value in extracted.items():
        if key != 'reference_source_sha256' and membership[key] != value:
            raise ValueError('Retained source excerpts disagree with membership: ' + key)

    presented = membership['presented_evaluation_ids_by_group']
    for group, keys in presented.items():
        if not set(keys) <= set(membership['evaluation_ids_by_group'][group]):
            raise ValueError('Presented evaluation identities lack extraction records: ' + group)
    detailed_analysis['presented_evaluation_summaries_by_group'] = {
        group: len(keys) for group, keys in presented.items()}
    detailed_analysis['evaluation_presentation'] = membership['evaluation_locations']

    inventory_by_id = {row['study_id']: row for row in membership['included_works']}
    write_csv(OUT / 'application-summaries.csv', [
        {'study_id': row['study_id'],
         'review_group': inventory_by_id[row['study_id']]['review_group'],
         'application': plain_text(row['application']),
         'reported_approach': plain_text(row['approach']),
         'source_table': inventory_by_id[row['study_id']]['source_table']}
        for row in summaries])
    platforms = platform_records(comparison_text)
    if {group: len(records) for group, records in platforms.items()} != snapshot['platform_counts']:
        raise ValueError('Platform comparison totals differ from the retained snapshot')
    for records in platforms.values():
        for record in records:
            record['references'] = []
            for key in record['reference_ids']:
                if key not in blocks:
                    raise ValueError('Platform reference is missing: ' + key)
                record['references'].append({
                    'id': key, 'title': plain_text(field(key, 'title')),
                    'url': field(key, 'url') or ('https://doi.org/' + field(key, 'doi')
                                               if field(key, 'doi') else ''),
                    'note': plain_text(field(key, 'note'))})
    artifacts['platform-comparisons.json'] = json_bytes(platforms)

    write_csv(OUT / 'survey-dataset.csv', collection)
    count_rows = [{'review_group': g, 'historical': hc[g], 'supplementary_update': uc[g],
                   'combined': cc[g]} for g in groups]
    count_rows.append({'review_group': 'total', 'historical': len(historical), 'supplementary_update': len(recent), 'combined': len(collection)})
    write_csv(OUT / 'study-counts.csv', count_rows)
    counts = {
        'artifact_date': DATE,
        'combined': {'application_studies': len(collection), 'by_group': dict(cc),
                     'group_interpretation': 'Accounting groups, not disjoint system-capability classes',
                     'contextual_references_counted_as_application_studies': False},
        'detailed_analysis': detailed_analysis,
        'research_questions': membership['research_questions'],
        'identity_validation': {'unique_citation_keys': len(collection), 'nonempty_dois': len(dois),
                            'unique_nonempty_dois': len(set(dois)),
                            'missing_dois': len(collection)-len(dois),
                            'unique_normalized_titles': len(set(titles))},
        'platform_comparisons': snapshot['platform_counts'],
    }
    artifacts['counts.json'] = json_bytes(counts)
    artifacts['application-references.bib'] = ('\n\n'.join(blocks[r['study_id']].strip() for r in collection)+'\n').encode('utf-8')

    if digest(artifacts['survey-dataset.csv']) != snapshot['canonical_dataset_sha256']:
        raise ValueError('Collection differs from the verified reference source dataset')
    eligibility = rows('revisao/protocol-eligibility.csv')
    included = [r['citation_key'] for r in eligibility if r['decision'] == 'include']
    if len(included) != len(scholar_retained) or set(included) != set(scholar_retained):
        raise ValueError('Ancillary eligibility records disagree with original Scholar inclusions')
    expected = snapshot['counts']
    if (expected['historical'], expected['recent'], expected['combined']) != (len(historical), len(recent), len(collection)):
        raise ValueError('Snapshot counts disagree with extraction')
    if expected['by_group'] != dict(cc):
        raise ValueError('Snapshot group counts disagree with records')
    if (expected['scholar_inclusions'], expected['additional_export_inclusions'], expected['targeted_followup_inclusions']) != (len(scholar_retained), len(additional), len(followup)):
        raise ValueError('Snapshot inclusion counts disagree with separate retrieval strata')
    if snapshot['complete_search'] or snapshot['complete_screening'] or snapshot['contextual_references_in_application_denominator']:
        raise ValueError('Snapshot overstates the documented scope')
    dictionary = json.loads((root / 'docs/data-dictionary.json').read_text(encoding='utf-8'))
    if set(dictionary) != set(collection[0]):
        raise ValueError('Data dictionary does not cover the dataset schema')

    annual = []
    for basis in ('extraction_year', 'bibliography_year'):
        years = sorted({r[basis] for r in collection}, key=int)
        for year in years:
            strata = Counter(r['collection'] for r in collection if r[basis] == year)
            annual.append({'year_basis': basis, 'year': year,
                           'historical': strata['historical'],
                           'supplementary_update': strata['supplementary_update'],
                           'combined': sum(strata.values())})
    artifacts['studies-by-year.csv'] = csv_bytes(annual, list(annual[0]))
    manifest = {
        'artifact_date': DATE,
        'generator': 'scripts/build_dataset.py',
        'scope': 'Artifact consistency, not independent screening or scientific validation',
        'inputs': {p.relative_to(root).as_posix(): digest(p.read_bytes()) for p in sorted([
            root / 'data/source-snapshot.json', root / 'docs/data-dictionary.json',
            root / 'scripts/build_dataset.py', root / 'scripts/source_tables.py',
            *[source_root / name for name in snapshot['source_files']],
        ])},
        'files': {name: digest(value) for name, value in sorted(artifacts.items())},
    }
    artifacts['manifest.json'] = json_bytes(manifest)
    return artifacts


def validate_artifacts(root, artifacts):
    problems = []
    for name, expected in artifacts.items():
        path = root / 'data' / name
        if not path.is_file():
            problems.append(f'Missing generated file: {name}')
        elif path.read_bytes() != expected:
            problems.append(f'Changed or stale generated file: {name}')
    if problems:
        raise ValueError('\n'.join(problems))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate', action='store_true', help='Validate sources and outputs without writing files')
    parser.add_argument('--check', dest='validate', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        artifacts = build_artifacts()
        if args.validate:
            validate_artifacts(ROOT, artifacts)
        else:
            # All input, identity and provenance checks complete before any output write.
            for name, payload in artifacts.items():
                path = ROOT / 'data' / name
                with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temp:
                    temporary = Path(temp.name)
                    temp.write(payload)
                try:
                    os.replace(temporary, path)
                finally:
                    temporary.unlink(missing_ok=True)
            validate_artifacts(ROOT, artifacts)
    except (ValueError, KeyError, IndexError, OSError, csv.Error) as exc:
        print(f'Dataset validation failed: {exc}', file=sys.stderr)
        return 1
    counts = json.loads(artifacts['counts.json'])
    print(json.dumps({'status': 'validated' if args.validate else 'rebuilt_and_validated',
                      'studies': counts['combined']['application_studies'],
                      'generated_files': len(artifacts),
                      'dataset_sha256': digest(artifacts['survey-dataset.csv'])}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
