import copy
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest

from scripts.build_dataset import ROOT, build_artifacts, digest
from scripts.reproduce_plots import validate_figure_outputs
from scripts.source_tables import (extract_membership, objective_sources, section_fragment,
                                   survey_method_fragment, table_fragment, table_rows)
from scripts.verify_source import verify


class SourceAndFigureTests(unittest.TestCase):
    def retained_source(self):
        source = ROOT / 'data/sources/revisao'
        return '\n\n'.join((source / name).read_text(encoding='utf-8') for name in
                            ('application-inventory.tex', 'comparison-excerpts.tex',
                             'survey-method.tex'))

    def test_multiline_objective_table_rejects_missing_and_duplicate_rows(self):
        heading = (r'\begin{table*}\label{tab:architecture-requirements}'
                   r'\begin{tabular}{lll}\toprule Objective & Observation & Assessment \\'
                   r'\midrule')
        rows = [r'\textbf{G' + str(i) + ': Objective}\n & '
                + r'Observation \cite{source' + str(i) + '}\n & '
                + r'Assessment \cite{context' + str(i) + r'} \\'
                for i in range(1, 9)]
        ending = r'\bottomrule\end{tabular}\end{table*}'
        expected = {f'G{i}': [f'source{i}', f'context{i}'] for i in range(1, 9)}
        self.assertEqual(objective_sources(heading + '\n'.join(rows) + ending), expected)
        with self.assertRaisesRegex(ValueError, 'Expected eight evaluation objectives'):
            objective_sources(heading + '\n'.join(rows[:-1]) + ending)
        with self.assertRaisesRegex(ValueError, 'Duplicate evaluation objective: G1'):
            objective_sources(heading + '\n'.join(rows + [rows[0]]) + ending)

    def test_root_relative_and_legacy_figure_paths_have_same_membership(self):
        source = self.retained_source()
        member = json.loads((ROOT / 'data/sources/revisao/collection-membership.json').read_text())
        root_relative = source.replace('{imgs/technology-timeline.pdf}', '{technology-timeline.pdf}')
        self.assertIn('{technology-timeline.pdf}', root_relative)
        legacy = root_relative.replace('{technology-timeline.pdf}', '{imgs/technology-timeline.pdf}')
        for candidate in (root_relative, legacy):
            parsed, _, _ = extract_membership(candidate.encode(), member['evaluation_ids_by_group'])
            self.assertEqual(parsed['current_plot_files'], ['technology-timeline.pdf'])

    def test_method_changes_are_rejected_without_relying_on_full_source_hash(self):
        source = self.retained_source()
        verify(source.encode(), external=False)
        method = survey_method_fragment(source)
        for old, new in [('139 publications', '138 publications'),
                         ('allintitle: blockchain data privacy',
                          'allintitle: blockchain data confidentiality')]:
            with self.subTest(changed=old):
                self.assertIn(old, method)
                altered = source.replace(method, method.replace(old, new, 1), 1)
                with self.assertRaisesRegex(ValueError, 'Survey Method differs'):
                    verify(altered.encode(), external=False)

    def test_evidence_changes_with_same_citation_ids_are_rejected(self):
        source = self.retained_source()
        verify(source.encode(), external=False)
        cases = [
            (section_fragment(source, 'sec:privacy-evaluation'),
             'The reviewed applications distinguish',
             'The reviewed applications do not distinguish', 'privacy synthesis differs'),
            (table_fragment(source, 'tab:consent-evaluation'),
             'Query and audit performance on synthetic data.',
             'Query and audit performance on real data.', 'tab:consent-evaluation'),
            (table_fragment(source, 'tab:worked-control-comparisons'),
             'Omitted events/secondary use unverified.',
             'Omitted events/secondary use verified.', 'tab:worked-control-comparisons'),
        ]
        for fragment, old, new, error in cases:
            with self.subTest(changed=old):
                self.assertIn(old, fragment)
                altered = source.replace(fragment, fragment.replace(old, new, 1), 1)
                with self.assertRaisesRegex(ValueError, error):
                    verify(altered.encode(), external=False)

    def test_external_platform_reference_preserves_full_source_hash_check(self):
        source = self.retained_source()
        tables = [table_fragment(source, label) for label in
                  ('tab:privacy-platforms', 'tab:ssi-platforms')]
        self.assertIn('Zcash', tables[0])
        changed_privacy = tables[0].replace('Zcash', 'Zcash reference source', 1)
        external_source = source.replace(tables[0], changed_privacy, 1).encode()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            retained = root / 'data/sources/revisao'
            retained.mkdir(parents=True)
            for name in ('application-inventory.tex', 'comparison-excerpts.tex', 'survey-method.tex'):
                (retained / name).write_bytes((ROOT / 'data/sources/revisao' / name).read_bytes())
            (retained / 'reference-platforms.tex').write_text(
                changed_privacy + '\n\n' + tables[1], encoding='utf-8')
            member = json.loads((ROOT / 'data/sources/revisao/collection-membership.json').read_text())
            member['reference_source_sha256'] = digest(external_source)
            (retained / 'collection-membership.json').write_text(json.dumps(member), encoding='utf-8')
            verify(external_source, root=root, external=True)
            with self.assertRaisesRegex(ValueError, 'platform descriptions differ'):
                verify(external_source, root=root, external=False)
            with self.assertRaisesRegex(ValueError, 'reference_source_sha256'):
                verify(source.encode(), root=root, external=True)

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
