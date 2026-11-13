import copy
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest

from scripts.build_dataset import ROOT, build_artifacts, digest
from scripts.reproduce_plots import validate_figure_outputs
from scripts.source_tables import extract_membership, table_rows


class SourceAndFigureTests(unittest.TestCase):
    def test_prose_evaluations_are_distinct_from_extraction_membership(self):
        source = ROOT / 'data/sources/revisao'
        member = json.loads((source / 'collection-membership.json').read_text())
        combined = b'\n\n'.join((source / name).read_bytes() for name in
                                ('application-inventory.tex', 'comparison-excerpts.tex'))
        parsed, _, _ = extract_membership(combined, member['evaluation_ids_by_group'])
        self.assertEqual(parsed['research_questions'], member['research_questions'])
        self.assertEqual(parsed['presented_evaluation_ids_by_group'],
                         member['presented_evaluation_ids_by_group'])
        self.assertEqual(len(parsed['presented_evaluation_ids_by_group']['privacy']), 7)
        self.assertEqual(len(member['evaluation_ids_by_group']['privacy']), 8)
        self.assertNotIn('updateHu2024InvisiReveal',
                         parsed['presented_evaluation_ids_by_group']['privacy'])
        self.assertIn('updateHu2024InvisiReveal', member['evaluation_ids_by_group']['privacy'])
        commented = b'% (RQ3) Incorrect question?\n' + combined
        self.assertEqual(extract_membership(commented, member['evaluation_ids_by_group'])[0]
                         ['research_questions'], member['research_questions'])

    def test_longtable_footer_order_does_not_create_a_data_row(self):
        for headers in (r'Header & Header \\ \endhead \endlastfoot',
                        r'\endlastfoot Header & Header \\ \endhead'):
            table = r'\begin{longtable}{ll}' + headers + r'Example & Value \\ \end{longtable}'
            self.assertEqual(table_rows(table), [['Example', 'Value']])

    def test_platform_and_application_exports_keep_all_rows_and_sources(self):
        artifacts = build_artifacts()
        rows = list(csv.DictReader(io.StringIO(artifacts['application-summaries.csv'].decode())))
        self.assertEqual(len(rows), 139)
        self.assertEqual(len({row['study_id'] for row in rows}), 139)
        platforms = json.loads(artifacts['platform-comparisons.json'])
        self.assertEqual({group: len(items) for group, items in platforms.items()},
                         {'privacy': 19, 'identity': 6})
        for items in platforms.values():
            for row in items:
                self.assertEqual(row['reference_ids'], [ref['id'] for ref in row['references']])
                self.assertTrue(row['references'])
                self.assertTrue(all(ref['title'] and ref['url'] for ref in row['references']))

    def test_period_values_are_recoverable_from_publication_annotations(self):
        source = ROOT / 'data/sources/revisao'
        with (source / 'technology-timeline-records.csv').open(newline='') as stream:
            records = list(csv.DictReader(stream))
        with (source / 'technology-timeline-periods.csv').open(newline='') as stream:
            periods = list(csv.DictReader(stream))
        features = ['HE', 'ABE', 'PRE', 'SEARCH', 'ZK', 'FL', 'DP',
                    'SSI', 'CREDENTIAL', 'INDY', 'VERAMO', 'IOTA']
        self.assertEqual(sum(any(int(row[f]) for f in features) for row in records), 62)
        for point in periods:
            start, end = int(point['period_start']), int(point['period_end'])
            selected = [row for row in records if start <= int(row['publication_year']) <= end]
            names = sorted(row['citation_key'] for row in selected if int(row[point['feature']]))
            self.assertEqual(int(point['count']), len(names))
            self.assertEqual(int(point['period_inventory']), len(selected))
            self.assertEqual(point['citation_keys'], ';'.join(names))
            self.assertAlmostEqual(float(point['percentage']), 100 * len(names) / len(selected), places=5)
        pre = next(row for row in periods if row['feature'] == 'PRE' and row['period_start'] == '2021')
        self.assertEqual(int(pre['count']), 4)

    def test_environment_difference_does_not_hide_altered_retained_figures(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            retained = {'python': '3.14.5', 'packages': {}, 'platform': {'system': 'A'},
                        'inputs': {'data': 'hash'}, 'outputs': {'plot.pdf': digest(b'original')}}
            (out / 'plot.pdf').write_bytes(b'original')
            (out / 'manifest.json').write_text(json.dumps(retained))
            current = copy.deepcopy(retained)
            current['platform'] = {'system': 'B'}
            current['outputs']['plot.pdf'] = digest(b'rendered')
            self.assertEqual(validate_figure_outputs(out, {'plot.pdf': b'rendered'}, current),
                             'different_rendering_environment')
            (out / 'plot.pdf').write_bytes(b'corrupted')
            with self.assertRaisesRegex(ValueError, 'altered retained figure'):
                validate_figure_outputs(out, {'plot.pdf': b'rendered'}, current)


if __name__ == '__main__':
    unittest.main()
