"""Regression checks for provenance, non-destructive processing and artifact drift."""
from collections import Counter
from pathlib import Path
import csv
import io
import json
import shutil
import tempfile
import unittest

from scripts.audit_legacy_exports import candidate_groups, normal_doi
from scripts.build_dataset import ROOT, ORIGINAL_UPDATE_KEYS, MEMBERSHIP_SOURCE, build_artifacts, check_artifacts, digest


class DuplicateAuditTests(unittest.TestCase):
    def test_different_studies_without_doi_are_not_grouped(self):
        records = [{'DOI': missing, 'Title': f'Distinct study {i}'}
                   for i, missing in enumerate(['', ' ', None, 'NaN', 'N/A'])]
        self.assertEqual(candidate_groups(records), [])

    def test_missing_titles_are_not_a_match(self):
        self.assertEqual(candidate_groups([{'DOI': '', 'Title': ''},
                                           {'DOI': None, 'Title': None}]), [])

    def test_normalized_nonempty_doi_matches_without_discarding_records(self):
        records = [{'DOI': 'https://doi.org/10.1000/ABC', 'Title': 'A study'},
                   {'DOI': ' DOI:10.1000/abc ', 'Title': 'Alternative title'}]
        before = json.dumps(records)
        groups = candidate_groups(records)
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]['match_basis'], 'nonempty_doi')
        self.assertEqual(len(groups[0]['records']), 2)
        self.assertEqual(json.dumps(records), before)
        self.assertEqual(normal_doi('https://dx.doi.org/10.1000/ABC'), '10.1000/abc')

    def test_title_match_with_different_dois_requires_review(self):
        groups = candidate_groups([
            {'DOI': '10.1000/a', 'Title': 'Same: Study'},
            {'DOI': '10.1000/b', 'Title': 'SAME study'},
        ])
        self.assertEqual(len(groups), 1)
        self.assertTrue(groups[0]['conflicting_nonempty_dois'])


class CollectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifacts = build_artifacts()

    def test_exact_manuscript_export_and_accounting(self):
        expected = json.loads((ROOT / 'data/source-snapshot.json').read_text())
        self.assertEqual(digest(self.artifacts['survey-dataset.csv']),
                         expected['canonical_dataset_sha256'])
        rows = list(csv.DictReader(io.StringIO(self.artifacts['survey-dataset.csv'].decode())))
        self.assertEqual(len(rows), expected['counts']['combined'])
        self.assertEqual(Counter(r['collection'] for r in rows),
                         {'historical': 98, 'supplementary_update': expected['counts']['recent']})
        self.assertTrue(ORIGINAL_UPDATE_KEYS <= {r['study_id'] for r in rows})
        nonempty_dois = [r['doi'] for r in rows if r['doi']]
        self.assertEqual(len(nonempty_dois), len(set(nonempty_dois)))
        for row in rows:
            if row['collection'] == 'supplementary_update':
                self.assertTrue(row['primary_text_evidence_location'])
                self.assertTrue(row['evidence_boundary'])
                self.assertTrue(row['native_record'])

    def test_pending_assessments_are_preserved(self):
        counts = json.loads(self.artifacts['counts.json'])['supplementary_update']
        self.assertFalse(counts['complete_search'])
        self.assertFalse(counts['complete_screening'])
        with (ROOT / 'data/sources/revisao/protocol-search-records.csv').open(newline='') as stream:
            observed = list(csv.DictReader(stream))
        decisions = Counter(r['decision'] for r in observed)
        self.assertEqual(counts['decision_counts'], dict(decisions))
        self.assertEqual(counts['pending_records'], decisions['candidate_full_text_assessment_not_completed'] + decisions['pending_primary_full_text'])
        self.assertEqual(counts['selected_studies'] + counts['pending_records'] + counts['excluded_application_records'] + sum(counts['other_recorded_dispositions'].values()), len(observed))

    def test_detailed_analysis_keeps_context_out_of_application_counts(self):
        counts = json.loads(self.artifacts['counts.json'])
        detail = counts['detailed_analysis']
        snapshot = json.loads((ROOT / 'data/source-snapshot.json').read_text())
        membership = json.loads((ROOT / 'data/sources' / MEMBERSHIP_SOURCE).read_text())
        included = {r['study_id'] for r in membership['included_works']}
        detailed = set(membership['detailed_example_ids'])
        context = set(membership['contextual_source_ids'])
        self.assertTrue(detailed <= included)
        self.assertFalse(included & context)
        self.assertFalse(detailed & context)
        self.assertEqual(detail['application_examples'], snapshot['counts']['detailed_application_examples'])
        self.assertEqual(detail['contextual_sources'], snapshot['counts']['contextual_sources'])
        self.assertEqual(detail['matrix_records'], len(detailed | context))
        self.assertEqual(detail['included_works_not_detailed'], len(included - detailed))
        self.assertEqual(detail['application_examples_by_group'], {'privacy': 12, 'consent': 27, 'identity': 11})
        self.assertEqual(detail['privacy_evaluation_summaries'], snapshot['counts']['privacy_evaluation_summaries'])
        self.assertFalse(detail['contextual_sources_in_application_denominator'])

    def copy_source_snapshot(self, root):
        snapshot = json.loads((ROOT / 'data/source-snapshot.json').read_text())
        files = ['data/source-snapshot.json', 'docs/data-dictionary.json',
                 'scripts/build_dataset.py',
                 *['data/sources/' + p for p in snapshot['source_files']],
                 *snapshot['legacy_csv_sha256']]
        for name in files:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def write_membership_with_updated_fingerprint(self, root, membership):
        path = root / 'data/sources' / MEMBERSHIP_SOURCE
        path.write_text(json.dumps(membership, indent=2) + '\n', encoding='utf-8')
        snapshot_path = root / 'data/source-snapshot.json'
        snapshot = json.loads(snapshot_path.read_text())
        snapshot['source_files'][MEMBERSHIP_SOURCE] = digest(path.read_bytes())
        snapshot_path.write_text(json.dumps(snapshot, indent=2) + '\n', encoding='utf-8')

    def test_contextual_source_cannot_enter_included_or_detailed_denominator(self):
        for target in ('included_works', 'detailed_example_ids'):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_source_snapshot(root)
                membership = json.loads((root / 'data/sources' / MEMBERSHIP_SOURCE).read_text())
                key = membership['contextual_source_ids'][0]
                if target == 'included_works':
                    membership[target].append({'study_id': key, 'review_group': 'privacy',
                                               'source_table': 'tab:privacy-works'})
                else:
                    membership[target][0] = key
                self.write_membership_with_updated_fingerprint(root, membership)
                with self.assertRaisesRegex(ValueError, 'Contextual sources cannot enter'):
                    build_artifacts(root)
                self.assertFalse((root / 'data/survey-dataset.csv').exists())

    def test_replacing_a_detailed_example_is_rejected_with_counts_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_source_snapshot(root)
            membership = json.loads((root / 'data/sources' / MEMBERSHIP_SOURCE).read_text())
            detailed = set(membership['detailed_example_ids'])
            replaced = membership['detailed_example_ids'][0]
            group = next(r['review_group'] for r in membership['included_works']
                         if r['study_id'] == replaced)
            replacement = next(r['study_id'] for r in membership['included_works']
                               if r['study_id'] not in detailed and r['review_group'] == group)
            membership['detailed_example_ids'][0] = replacement
            self.write_membership_with_updated_fingerprint(root, membership)
            with self.assertRaisesRegex(ValueError, 'Detailed application membership differs from synthesis matrix'):
                build_artifacts(root)
            self.assertFalse((root / 'data/survey-dataset.csv').exists())

    def test_each_annual_basis_counts_each_study_once(self):
        rows = csv.DictReader(io.StringIO(self.artifacts['studies-by-year.csv'].decode()))
        totals = Counter()
        for row in rows:
            totals[row['year_basis']] += int(row['combined'])
        expected = json.loads((ROOT / 'data/source-snapshot.json').read_text())['counts']['combined']
        self.assertEqual(totals, {'extraction_year': expected, 'bibliography_year': expected})

    def test_retrieved_candidates_are_separate_from_included_studies(self):
        counts = json.loads(self.artifacts['counts.json'])
        status = json.loads((ROOT / 'data/sources/revisao/search-completion-status.json').read_text())
        self.assertEqual(counts['additional_retrieval'], status)
        self.assertEqual(sum(status['raw_observations_by_query'].values()), status['raw_observations'])
        self.assertFalse(status['complete_scientific_screening'])
        with (ROOT / 'data/sources/revisao/search-completion-candidates-metadata.csv').open(newline='', encoding='utf-8') as stream:
            candidates = list(csv.DictReader(stream))
        self.assertEqual(len(candidates), status['consolidated_candidates'])
        self.assertEqual(len({r['record_id'] for r in candidates}), len(candidates))
        self.assertEqual(dict(Counter(r['decision'] for r in candidates)), status['decision_counts'])
        self.assertNotEqual(counts['combined']['application_studies'], len(candidates))
        self.assertNotIn('abstract_indexed', candidates[0])

    def test_output_corruption_is_detected_without_repair(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'data').mkdir()
            for name, payload in self.artifacts.items():
                (root / 'data' / name).write_bytes(payload)
            path = root / 'data/survey-dataset.csv'
            path.write_bytes(b'corrupted dataset\n')
            with self.assertRaisesRegex(ValueError, 'Changed or stale generated file'):
                check_artifacts(root, self.artifacts)
            self.assertEqual(path.read_bytes(), b'corrupted dataset\n')

    def test_snapshot_rejects_changed_source_and_changed_legacy_file(self):
        snapshot = json.loads((ROOT / 'data/source-snapshot.json').read_text())
        for changed in ('data/sources/revisao/recent-extraction.csv', 'privacy/google.csv'):
            with self.subTest(changed=changed), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                files = ['data/source-snapshot.json',
                         *['data/sources/' + p for p in snapshot['source_files']],
                         *snapshot['legacy_csv_sha256']]
                for name in files:
                    target = root / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(ROOT / name, target)
                (root / changed).write_bytes(b'changed\n')
                with self.assertRaisesRegex(ValueError, 'Source differs|Historical CSV changed'):
                    build_artifacts(root)
                self.assertFalse((root / 'data/survey-dataset.csv').exists())


if __name__ == '__main__':
    unittest.main()
