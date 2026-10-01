"""Export the documented study collection and a count-driven vector figure.

No retrieval or screening is performed here. Run export_and_validate.py first
when the manuscript tables have changed, then run this script with the bundled
Python runtime. Counts come from the extraction and observed-query records.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re
import shutil
import zipfile

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import simpleSplit

ROOT = Path(__file__).resolve().parent.parent
DATE = '2026-10-01'
ORIGINAL_UPDATE_KEYS = {
    'updateMasood2024Patient', 'updateCan2024AuditableConsent',
    'updateJaved2024SecureConsent', 'updatePhuyal2026Architecture',
    'updateZeydan2024SSI', 'updateAgarkar2024BADIMAC',
    'updateMaZhang2024Rollup', 'updateDhasaratha2024IoMT',
}
OUT = ROOT / 'output/dataset' / f'survey-dataset-{DATE}'
OUT.mkdir(parents=True, exist_ok=True)

def rows(path):
    with (ROOT / path).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def write_csv(path, records, columns=None):
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns or list(records[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(records)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

bib = (ROOT / 'references-revised.bib').read_text(encoding='utf-8')
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
additions_path = ROOT / 'revisao/update-assessment-additions.csv'
addition_keys = {r['citation_key'] for r in rows('revisao/update-assessment-additions.csv')} if additions_path.exists() else set()
observed = rows('revisao/protocol-search-records.csv')
retrieval_status = json.loads((ROOT / 'revisao/protocol-retrieval-status.json').read_text(encoding='utf-8'))
expansion_status_path = ROOT / 'revisao/search-completion-status.json'
expansion_status = json.loads(expansion_status_path.read_text(encoding='utf-8')) if expansion_status_path.exists() else {}
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
            'source_table': record['source_table'] if is_old else (record.get('source_table') or ('tab:focused-update-additions' if key in addition_keys else 'tab:focused-update')),
            'source_extraction_file': source,
            'source_record_number': record_number,
            'verification_scope': record['verification_scope'] if is_old else
                'Primary text and publication identity checked for extracted descriptions; '
                'author claims qualified; no independent reproduction or compliance certification',
        })

assert len(historical) == 98 and len(recent) == len(retained)
assert ORIGINAL_UPDATE_KEYS <= set(retained), 'Original eight update studies must be retained'
assert {r['citation_key'] for r in recent} == set(retained)
assert len(collection) == len({r['study_id'] for r in collection}) == len(historical) + len(recent)
hc = Counter(r['historical_group'] for r in historical)
uc = Counter(query_groups[r['query_id']] for r in retained.values())
cc = Counter(r['review_group'] for r in collection)
assert hc == {'privacy': 40, 'consent': 33, 'identity': 25}
assert cc == hc + uc
dois = [r['doi'] for r in collection if r['doi']]
titles = [re.sub(r'[^a-z0-9]', '', r['title_bibtex'].lower()) for r in collection]
assert len(dois) == len(set(dois)), 'Duplicate nonempty DOI in application collection'
assert len(titles) == len(set(titles)), 'Duplicate normalized title in application collection'
decisions = Counter(r['decision'] for r in observed)
assert len(observed) == 50
assert Counter(r['query_id'] for r in observed) == {'S01': 10, 'S04': 30, 'S07': 10}
assert decisions['retained_after_primary_text_check'] == len(recent)
excluded = {k: v for k, v in decisions.items() if k.startswith('excluded_')}
pending = decisions['candidate_full_text_assessment_not_completed'] + decisions['pending_primary_full_text']
other = {k: v for k, v in decisions.items() if k not in {
    'retained_after_primary_text_check', 'candidate_full_text_assessment_not_completed',
    'pending_primary_full_text'} and k not in excluded}
assert len(recent) + pending + sum(excluded.values()) + sum(other.values()) == len(observed)

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
    'identity_checks': {'unique_citation_keys': len(collection), 'nonempty_dois': len(dois),
                        'unique_nonempty_dois': len(set(dois)),
                        'missing_dois': len(collection)-len(dois),
                        'unique_normalized_titles': len(set(titles)),
                        'scope': 'Metadata identity checks; not new independent review of all historical studies'},
}
(OUT / 'counts.json').write_text(json.dumps(counts, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
(OUT / 'application-references.bib').write_text('\n\n'.join(blocks[r['study_id']].strip() for r in collection)+'\n', encoding='utf-8')

# Preserve evidence in its source schema alongside the normalized export.
source_paths = [
    'historical-extraction.csv', 'revisao/recent-extraction.csv',
    'revisao/protocol-search-records.csv', 'revisao/protocol-eligibility.csv',
    'revisao/protocol-retrieval-status.json', 'revisao/historical-method-audit.md',
    'revisao/literature-search-log.md', 'revisao/retry-access-log.md',
    'revisao/bibliography-normalization.json', 'revisao/build_updated_dataset.py',
    'revisao/qualitative-survey-scope.md',
    'revisao/governance-framing-evidence.md', 'revisao/governance-sources.bib',
    'revisao/architecture-context-sources.bib', 'revisao/architecture-synthesis-evidence.md',
]
optional_sources = [
    'revisao/update-assessment-additions.csv',
    'revisao/update-assessment-additions.bib',
    'revisao/synthesis-evidence-matrix.csv', 'revisao/synthesis-evidence-method.md',
    'revisao/synthesis-evidence-coverage.json',
    'revisao/update-assessment-2026-10-01.csv', 'revisao/update-assessment-2026-10-01.md',
    'revisao/contextual-evidence-expansion.md', 'revisao/policy-context-sources.bib',
    'revisao/contextual-verification-additions.bib',
    'revisao/analysis-expansion-before.json',
    'revisao/analysis-expansion-preservation.json',
    'revisao/recent-extraction-before-assessment.csv',
    'revisao/protocol-search-records-before-assessment.csv',
    'revisao/search-completion-inclusions.csv', 'revisao/search-completion-inclusions.bib',
    'revisao/search-completion-inclusions.json', 'revisao/search-completion-publication-metadata.json',
    'revisao/search-completion-primary-evidence.md', 'revisao/search-completion-2026-10-01.md',
    'revisao/search-completion-candidates.csv', 'revisao/search-completion-status.json',
    'revisao/consolidate_search_completion.py', 'revisao/integrate_search_completion.py',
]
optional_sources.extend(p.relative_to(ROOT).as_posix() for p in
                        sorted((ROOT / 'revisao').glob('search-expansion-*20261001*'))
                        if p.suffix in {'.csv', '.tsv'})
source_paths.extend(name for name in optional_sources if (ROOT / name).exists())
for name in source_paths:
    target = OUT / 'sources' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / name, target)

dictionary = {
    'study_id': 'Stable bibliography citation key. One included application study per row.',
    'collection': 'historical or supplementary_update; preserve the two provenance strata.',
    'review_group': 'privacy, consent, identity; accounting only, not exclusive technical capabilities.',
    'group_basis': 'Historical extracted group, or observed original-query family for recent additions.',
    'title_bibtex': 'Title from canonical bibliography. BibTeX braces/escapes retained.',
    'authors_bibtex': 'Authors from canonical bibliography; BibTeX and separator semantics retained.',
    'extraction_year': 'Historical table year or recent extraction year; not always final issue year.',
    'bibliography_year': 'Year in canonical bibliography; differences do not create additional studies.',
    'doi': 'Normalized nonempty DOI. Blank means not identified in the canonical entry; blanks never deduplicated together.',
    'publication_url': 'DOI resolver URL when DOI exists; otherwise bibliography URL if present. Not proof of full-text access.',
    'application': 'Use case as recorded in source extraction.',
    'reported_approach': 'Described mechanism. Some historical groups did not extract a separate mechanism field.',
    'reported_contribution': 'Source-extraction description, not independent endorsement of a claim.',
    'reported_platform': 'Platform field inherited from source; historical operational status not fully revalidated.',
    'reported_software_link': 'Availability observation only. N/A or not identified does not prove no implementation exists.',
    'reported_evaluation': 'Recent-study evaluation description; blank historical values mean not uniformly extracted.',
    'evidence_boundary': 'Recent-study limitations; blank historical values do not mean absence of limitations.',
    'primary_text_source_url': 'Recent primary-text access source; blank historical field is unpopulated, not evidence of absence.',
    'primary_text_evidence_location': 'Recent section/table/page attribution; not uniformly available for historical studies.',
    'query_id_observed': 'Recent native query identifier; not retrospectively assigned to historical selections.',
    'native_record': 'Recent query/rank/page linkage to the 50 observed records.',
    'source_table': 'LaTeX label of the manuscript table containing the study.',
    'source_extraction_file': 'Original CSV supplying the study-specific extracted fields.',
    'source_record_number': 'One-based data-record index in that CSV, excluding header; not physical line number.',
    'verification_scope': 'Explicit distinction between inherited historical extraction and checked recent descriptions.',
}
(OUT / 'data-dictionary.json').write_text(json.dumps(dictionary, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

# A new vector count diagram, generated from the same values as the dataset.
# This is a collection inventory, not a reconstructed PRISMA/search flow.
PDF = ROOT / 'output/pdf/selection-criteria-updated.pdf'
PDF.parent.mkdir(parents=True, exist_ok=True)
W, H = 640, 412
c = canvas.Canvas(str(PDF), pagesize=(W, H), invariant=1)
c.setTitle('Documented application study collection')
c.setAuthor('Survey revision: generated from documented extraction records')
ink, muted, rule = HexColor('#183342'), HexColor('#50626e'), HexColor('#c4cfd4')
blue, teal, pale = HexColor('#edf3f8'), HexColor('#e3f1ed'), HexColor('#f6f7f8')

def text(x, y, value, size=10, bold=False, color=ink):
    c.setFillColor(color); c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    c.drawString(x, y, value)

def wrapped(x, y, value, width, size=9, leading=12, color=muted):
    for line in simpleSplit(value, 'Helvetica', size, width):
        text(x, y, line, size=size, color=color); y -= leading
    return y

def box(x, y, w, h, fill):
    c.setFillColor(fill); c.setStrokeColor(rule); c.setLineWidth(.7)
    c.roundRect(x, y, w, h, radius=5, stroke=1, fill=1)

text(18, 390, 'Blockchain-assisted data sharing: application collection', 16, True)
box(18, 282, 604, 85, teal)
text(36, 322, str(len(collection)), 35, True)
text(125, 331, 'application records', 17, True)
text(125, 305, 'Privacy, consent, and decentralized identity in one thematic comparison', 11)
for x, label, group in [(18, 'PRIVACY', 'privacy'), (224, 'CONSENT', 'consent'), (430, 'IDENTITY / SSI', 'identity')]:
    box(x, 166, 192, 94, blue)
    text(x+14, 236, label, 11, True)
    text(x+14, 192, str(cc[group]), 29, True)
text(18, 145, 'Search-family groups are not mutually exclusive classes of system capabilities.', 10, color=muted)
box(18, 35, 604, 93, pale)
text(32, 108, 'COVERAGE AND EVIDENCE LIMITS', 10, True)
wrapped(32, 90, 'Title-only searches limit coverage. Scopus and ACM Full-Text Collection queries were executed. Google Scholar pagination and assessment of additional retrieved candidates remain incomplete.', 570, 10, 13)
text(32, 47, f'{pending} original observed record remains pending. Additional candidates await screening.', 10)
text(18, 16, f'{len(collection)} application records; contextual sources are excluded. This is an inventory, not a PRISMA flow.', 9, color=muted)
c.showPage(); c.save()
shutil.copy2(PDF, OUT / PDF.name)

group_table = '\n'.join(f'| {group.title()} | {hc[group]} | {uc[group]} | {cc[group]} |' for group in groups)
decision_table = '\n'.join(f'| {decision} | {number} |' for decision, number in decisions.items())
README = f"""# Documented survey dataset — {DATE}

This package accompanies **Governance of Blockchain-Assisted Data Sharing: A Survey of Privacy, Consent, and Self-Sovereign Identity**, a structured qualitative survey. Its scope and rationale are recorded in `sources/revisao/qualitative-survey-scope.md`. It documents criteria, searches, extraction and limitations, rather than exhaustive systematic coverage or a reconstructed historical screening flow.

The public data repository is [rodrigodg1/blockchain-survey](https://github.com/rodrigodg1/blockchain-survey).

## Application-study collection

`survey-dataset.csv` contains **{len(collection)} application studies: {len(historical)} historical and {len(recent)} supplementary-update studies**. It uses UTF-8, comma separation, a header and one logical row per study. Preserve the `collection` provenance strata.

| Accounting group | Historical | Update | Combined |
|---|---:|---:|---:|
{group_table}
| Total | {len(historical)} | {len(recent)} | {len(collection)} |

Groups reflect the historical extraction or the observed retrieval-query family. They are not mutually exclusive classes of technical capabilities and cannot estimate how many systems integrate every topic. Standards, regulators, platforms, related surveys and contextual sources are outside the application-study denominator.

## Observed update records and current decisions

The 30 September 2026 retrieval observed {len(observed)} Google Scholar records: S01 page 1, S04 pages 1–3, S07 page 1. Assessment records document later decisions without changing that retrieval denominator.

| Current recorded decision | Observed records |
|---|---:|
{decision_table}

Current accounting is {len(recent)} included applications, {sum(excluded.values())} concluded application exclusions, {pending} pending assessments/texts and {sum(other.values())} other dispositions. Pending records are not exclusions. The observed records are not the complete search results across the three databases and are not a count of unique studies discovered.

Scopus title queries S02/S05/S08 were executed on 1 October 2026 and all 496/47/175 observations were exported. ACM title queries S03/S06/S09 retrieved 15/12/8 observations from the Full-Text Collection. The Guide to Computing Literature was not searched. Google Scholar pagination and scientific assessment of the additional candidates remain incomplete. `sources/revisao/search-completion-status.json` reports the retained raw observations and consolidation counts. These counts do not reconstruct the original collection's retrieval or screening history. The figure is a collection inventory, not a complete PRISMA flow.

## Files and evidence

- `survey-dataset.csv`: consolidated extraction, bibliographic metadata, provenance and limits.
- `study-counts.csv`, `counts.json`: count-driven collection and disposition summaries.
- `search-decision-counts.csv`: current decisions for the preserved observed records.
- `application-references.bib`: bibliography entries for the {len(collection)} application studies.
- `data-dictionary.json`: field meanings and missing-value semantics.
- `selection-criteria-updated.pdf`: vector inventory generated from the same counts.
- `sources/`: source-schema extractions, methodological records and contextual synthesis evidence when available.
- `manifest.json`: SHA-256 fingerprints of every packaged file and input.

The 98 historical identities and the original eight update identities are preserved. Newly retained records require matching native retrieval decisions, primary-text locations and the same title/year predicates. Synthesis examples and contextual references are not automatically application additions. The generator performs no searching, screening or independent reproduction.

The current metadata checks cover {len(collection)} unique citation keys, {len(set(dois))} unique nonempty DOIs, {len(collection)-len(dois)} entries without DOI and {len(set(titles))} distinct normalized titles. Missing DOI values are not deduplication keys.

Historical blank evaluation/source-location fields mean they were not uniformly extracted, not that evidence or limitations are absent. BibTeX fields retain braces and escapes; extraction fields may retain LaTeX notation. Extraction and bibliography years can differ without creating another study.

## Reproduction

After manuscript table edits, compile the manuscript and run `revisao/export_and_validate.py`, then `revisao/build_updated_dataset.py` with Python, pypdf and ReportLab, followed by `revisao/validate_updated_dataset.py`. Identities, provenance, disposition accounting and arithmetic are checked before export. Do not rerun old manuscript-rewrite scripts to recreate this package.
"""
(OUT / 'README.md').write_text(README, encoding='utf-8')

manifest = {
    'generated_on': DATE,
    'generator': 'revisao/build_updated_dataset.py',
    'input_sha256': {name: digest(ROOT / name) for name in source_paths + ['references-revised.bib', 'main.tex']},
    'files': {p.relative_to(OUT).as_posix(): digest(p) for p in sorted(OUT.rglob('*'))
              if p.is_file() and p.name != 'manifest.json'},
}
(OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
archive = OUT.with_suffix('.zip')
archive_temporary = OUT.with_suffix('.zip.tmp')
with zipfile.ZipFile(archive_temporary, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for path in sorted(OUT.rglob('*')):
        if path.is_file():
            z.write(path, path.relative_to(OUT.parent).as_posix())
archive_temporary.replace(archive)
print(json.dumps({'dataset_rows': len(collection), 'counts': count_rows,
                  'observed_records': len(observed), 'figure': str(PDF),
                  'archive': str(archive)}, ensure_ascii=False))
