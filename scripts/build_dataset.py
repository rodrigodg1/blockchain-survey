"""Rebuild the documented survey snapshot; no searching or screening.

The collection mapping is adapted from revisao/build_updated_dataset.py in the
revised manuscript workspace. This portable edition uses only Python's standard
library, generates no figures, and checks the imported source snapshot.
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

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_UPDATE_KEYS = {
    'updateMasood2024Patient', 'updateCan2024AuditableConsent',
    'updateJaved2024SecureConsent', 'updatePhuyal2026Architecture',
    'updateZeydan2024SSI', 'updateAgarkar2024BADIMAC',
    'updateMaZhang2024Rollup', 'updateDhasaratha2024IoMT',
}
MEMBERSHIP_SOURCE = 'revisao/manuscript-membership.json'
MATRIX_SOURCE = 'revisao/synthesis-evidence-matrix.csv'
APPLICATION_MATRIX_ROLES = {
    'historical_application', 'recent_application',
    'recent_application_addition', 'recent_application_search_completion',
}


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
    for name, expected in snapshot['legacy_csv_sha256'].items():
        if digest((root / name).read_bytes()) != expected:
            raise ValueError(f'Historical CSV changed: {name}')
    return snapshot


def validate_manuscript_membership(collection, matrix, recent, retained, snapshot, membership):
    if membership['manuscript_sha256'] != snapshot['manuscript_sha256']:
        raise ValueError('Manuscript membership fingerprint differs from source snapshot')

    def unique_ids(values, description):
        if any(not isinstance(key, str) or not key.strip() for key in values):
            raise ValueError(f'Invalid identity in {description}')
        if len(values) != len(set(values)):
            raise ValueError(f'Duplicate identities in {description}')
        return set(values)

    works = membership['included_works']
    included_ids = unique_ids([r['study_id'] for r in works], 'manuscript application membership')
    detailed_ids = unique_ids(membership['detailed_example_ids'], 'detailed application membership')
    contextual_ids = unique_ids(membership['contextual_source_ids'], 'contextual membership')
    privacy_evaluation_ids = unique_ids(membership['privacy_evaluation_ids'], 'privacy evaluation membership')
    collection_by_id = {r['study_id']: r for r in collection}
    if contextual_ids & (included_ids | detailed_ids | set(collection_by_id)):
        raise ValueError('Contextual sources cannot enter included or detailed application membership')
    if included_ids != set(collection_by_id):
        raise ValueError('Included application membership differs from manuscript')
    for work in works:
        row = collection_by_id[work['study_id']]
        if (work['review_group'], work['source_table']) != (row['review_group'], row['source_table']):
            raise ValueError('Manuscript group or table differs for study: ' + work['study_id'])
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

    expected_privacy = {r['citation_key'] for r in recent
                        if retained[r['citation_key']]['query_id'] == 'S01'
                        and r['evaluation'].strip()}
    if privacy_evaluation_ids != expected_privacy:
        raise ValueError('Privacy evaluation membership differs from primary extraction')
    if not privacy_evaluation_ids <= detailed_ids:
        raise ValueError('Privacy evaluation summaries must belong to the detailed application examples')
    expected = snapshot['counts']
    if (len(detailed_ids), len(contextual_ids), len(privacy_evaluation_ids)) != (
            expected['detailed_application_examples'], expected['contextual_sources'],
            expected['privacy_evaluation_summaries']):
        raise ValueError('Snapshot detailed/contextual/evaluation counts disagree with membership')

    return {
        'application_examples': len(detailed_ids),
        'contextual_sources': len(contextual_ids),
        'matrix_records': len(matrix_ids),
        'included_works_not_detailed': len(included_ids - detailed_ids),
        'application_examples_by_group': dict(Counter(collection_by_id[key]['review_group']
                                                     for key in sorted(detailed_ids))),
        'privacy_evaluation_summaries': len(privacy_evaluation_ids),
        'contextual_sources_in_application_denominator': False,
        'scope': 'Source-linked qualitative comparisons; not uniform assessment of all included works',
    }


def build_artifacts(root=ROOT):
    root = Path(root)
    snapshot = load_snapshot(root)
    source_root = root / 'data/sources'
    for name in (MEMBERSHIP_SOURCE, MATRIX_SOURCE):
        if name not in snapshot['source_files']:
            raise ValueError('Required membership source is not fingerprinted in snapshot: ' + name)
    membership = json.loads((source_root / MEMBERSHIP_SOURCE).read_text(encoding='utf-8'))
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
    observed = rows('revisao/protocol-search-records.csv')
    retrieval_status = json.loads((source_root / 'revisao/protocol-retrieval-status.json').read_text(encoding='utf-8'))
    expansion_status = json.loads((source_root / 'revisao/search-completion-status.json').read_text(encoding='utf-8'))
    retained = {r['citation_key']: r for r in observed
                if r['decision'] == 'retained_after_primary_text_check'}
    query_groups = {'S01': 'privacy', 'S04': 'consent', 'S07': 'identity'}
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
    decisions = Counter(r['decision'] for r in observed)
    if not (len(observed) == 50):
        raise ValueError('Invalid source data: len(observed) == 50')
    if not (Counter(r['query_id'] for r in observed) == {'S01': 10, 'S04': 30, 'S07': 10}):
        raise ValueError("Invalid source data: Counter((r['query_id'] for r in observed)) == {'S01': 10, 'S04': 30, 'S07': 10}")
    if decisions['retained_after_primary_text_check'] != len(recent):
        raise ValueError('Retained decision count disagrees with included studies')
    excluded = {k: v for k, v in decisions.items() if k.startswith('excluded_')}
    pending = decisions['candidate_full_text_assessment_not_completed'] + decisions['pending_primary_full_text']
    other = {k: v for k, v in decisions.items() if k not in {
        'retained_after_primary_text_check', 'candidate_full_text_assessment_not_completed',
        'pending_primary_full_text'} and k not in excluded}
    if len(recent) + pending + sum(excluded.values()) + sum(other.values()) != len(observed):
        raise ValueError('Disposition categories do not account for all observed records')

    detailed_analysis = validate_manuscript_membership(
        collection, rows(MATRIX_SOURCE), recent, retained, snapshot, membership)

    write_csv(OUT / 'survey-dataset.csv', collection)
    count_rows = [{'review_group': g, 'historical': hc[g], 'supplementary_update': uc[g],
                   'combined': cc[g]} for g in groups]
    count_rows.append({'review_group': 'total', 'historical': len(historical), 'supplementary_update': len(recent), 'combined': len(collection)})
    write_csv(OUT / 'study-counts.csv', count_rows)
    write_csv(OUT / 'search-decision-counts.csv',
              [{'decision': k, 'observed_records': v} for k, v in decisions.items()])
    counts = {
        'artifact_date': DATE, 'study_update_search_date': '2026-09-30',
        'historical': {'selected_studies': 98, 'by_group': dict(hc),
                       'complete_retrieval_and_screening_counts_reconstructed': False},
        'supplementary_update': {
            'year_filter': '2024-2026', 'observed_query_records': len(observed),
            'query_record_counts': dict(Counter(r['query_id'] for r in observed)),
            'selected_studies': len(recent), 'selected_by_group': dict(uc),
            'decision_counts': dict(decisions), 'other_recorded_dispositions': other,
            'excluded_application_records': sum(excluded.values()), 'excluded_decision_counts': excluded,
            'pending_records': pending,
            'coverage': 'Partial Google Scholar retrieval: S01 page 1, S04 pages 1-3, S07 page 1',
            'Scopus': retrieval_status['Scopus'],
            'ACM_DL': retrieval_status['ACM_DL'],
            'complete_search': False, 'complete_screening': False,
        },
        'additional_retrieval': expansion_status,
        'combined': {'application_studies': len(collection), 'by_group': dict(cc),
                     'group_interpretation': 'Accounting groups, not disjoint system-capability classes',
                     'contextual_references_counted_as_application_studies': False},
        'detailed_analysis': detailed_analysis,
        'identity_checks': {'unique_citation_keys': len(collection), 'nonempty_dois': len(dois),
                            'unique_nonempty_dois': len(set(dois)),
                            'missing_dois': len(collection)-len(dois),
                            'unique_normalized_titles': len(set(titles)),
                            'scope': 'Metadata identity checks; not new independent review of all historical studies'},
    }
    artifacts['counts.json'] = json_bytes(counts)
    artifacts['application-references.bib'] = ('\n\n'.join(blocks[r['study_id']].strip() for r in collection)+'\n').encode('utf-8')

    if digest(artifacts['survey-dataset.csv']) != snapshot['canonical_dataset_sha256']:
        raise ValueError('Collection differs from the verified manuscript dataset')
    eligibility = rows('revisao/protocol-eligibility.csv')
    included = [r['citation_key'] for r in eligibility if r['decision'] == 'include']
    if len(included) != len(retained) or set(included) != set(retained):
        raise ValueError('Eligibility records disagree with included update studies')
    status = json.loads((source_root / 'revisao/protocol-retrieval-status.json').read_text(encoding='utf-8'))
    if status['decision_counts'] != counts['supplementary_update']['decision_counts']:
        raise ValueError('Retrieval summary disagrees with query records')
    if status['retrieved_result_records'] != len(observed) or status['included_primary_studies'] != len(recent):
        raise ValueError('Retrieval summary counts disagree with extraction')
    expected = snapshot['counts']
    if (expected['historical'], expected['recent'], expected['combined'], expected['observed_records']) != (len(historical), len(recent), len(collection), len(observed)):
        raise ValueError('Snapshot counts disagree with extraction')
    if expected['by_group'] != dict(cc) or expected['pending_records'] != pending:
        raise ValueError('Snapshot group/pending counts disagree with records')
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
            root / 'scripts/build_dataset.py',
            *[source_root / name for name in snapshot['source_files']],
            *[root / name for name in snapshot['legacy_csv_sha256']],
        ])},
        'files': {name: digest(value) for name, value in sorted(artifacts.items())},
    }
    artifacts['manifest.json'] = json_bytes(manifest)
    return artifacts


def check_artifacts(root, artifacts):
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
    parser.add_argument('--check', action='store_true', help='Validate sources and outputs without writing files')
    args = parser.parse_args(argv)
    try:
        artifacts = build_artifacts()
        if args.check:
            check_artifacts(ROOT, artifacts)
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
            check_artifacts(ROOT, artifacts)
    except (ValueError, KeyError, IndexError, OSError, csv.Error) as exc:
        print(f'Dataset validation failed: {exc}', file=sys.stderr)
        return 1
    counts = json.loads(artifacts['counts.json'])
    print(json.dumps({'status': 'validated' if args.check else 'rebuilt_and_validated',
                      'studies': counts['combined']['application_studies'],
                      'historical': counts['historical']['selected_studies'],
                      'recent': counts['supplementary_update']['selected_studies'],
                      'generated_files': len(artifacts),
                      'dataset_sha256': digest(artifacts['survey-dataset.csv'])}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
