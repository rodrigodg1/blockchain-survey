"""Read-only inventory of historical retrieval exports; never selects studies."""
from collections import defaultdict
from pathlib import Path
import csv
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
MISSING = {'', 'nan', 'none', 'null', 'n/a', 'na'}


def normal_doi(value):
    value = (value or '').strip().lower()
    value = re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)', '', value)
    return '' if value in MISSING else value


def normal_title(value):
    value = unicodedata.normalize('NFKC', value or '').casefold()
    return ''.join(c for c in value if c.isalnum())


def candidate_groups(records):
    """Report possible matches; blank identifiers never create a match."""
    indexes = {'nonempty_doi': defaultdict(list), 'normalized_title': defaultdict(list)}
    for position, row in enumerate(records):
        for kind, key in [('nonempty_doi', normal_doi(row.get('DOI'))),
                          ('normalized_title', normal_title(row.get('Title')))]:
            if key:
                indexes[kind][key].append(position)
    result = []
    for kind, groups in indexes.items():
        for key, positions in groups.items():
            if len(positions) < 2:
                continue
            dois = {normal_doi(records[p].get('DOI')) for p in positions}
            dois.discard('')
            result.append({
                'match_basis': kind,
                'normalized_value': key,
                'records': [{'file': records[p].get('_source_file', ''),
                             'record_number': records[p].get('_source_record', p + 1),
                             'title': records[p].get('Title', ''),
                             'doi': records[p].get('DOI', '')} for p in positions],
                'conflicting_nonempty_dois': len(dois) > 1,
            })
    return result


def audit(root=ROOT):
    root = Path(root)
    result = {'scope': 'Historical retrieval records, not the selected application collection',
              'records_removed': 0, 'families': {}}
    for family in ('privacy', 'consent', 'identity'):
        records, inventory = [], []
        for source in ('google', 'scopus', 'acm'):
            name = f'{family}/{source}.csv'
            with (root / name).open(encoding='utf-8-sig', newline='') as stream:
                rows = list(csv.DictReader(stream))
            inventory.append({'file': name, 'records': len(rows),
                              'missing_dois': sum(not normal_doi(r.get('DOI')) for r in rows)})
            records.extend(dict(row, _source_file=name, _source_record=i)
                           for i, row in enumerate(rows, 1))
        groups = candidate_groups(records)
        result['families'][family] = {
            'files': inventory, 'concatenated_records': len(records),
            'candidate_groups': groups,
            'note': 'Groups can overlap. Do not subtract them to infer unique or selected study counts.',
        }
    return result


if __name__ == '__main__':
    print(json.dumps(audit(), indent=2, ensure_ascii=False))
