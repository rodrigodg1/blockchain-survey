# Maintaining the documented snapshot

The current release matches the 1 October 2026 manuscript snapshot: **136 application records**, with 98 retained and 38 recent source records. Primary assessment added 14 applications and reduced the original pending set to one. Scopus/ACM retrieval is documented separately from the unfinished additional-candidate screening. The builder exports a documented selection. It performs no crawling or scientific screening.

## Rebuilding unchanged inputs

Run `python3 run.py`, followed by `python3 run.py --check`. Both commands validate the source fingerprints and identities before accepting the exported collection. The check compares every generated file with its in-memory reconstruction and fails on missing, modified or stale output. The output manifest records the generator, dictionary, source inputs and preserved historical CSVs.

The seven generated files are `survey-dataset.csv`, `study-counts.csv`, `search-decision-counts.csv`, `counts.json`, `application-references.bib`, `studies-by-year.csv` and `manifest.json`, all under `data/`. Do not edit them manually.

## Incorporating a subsequent manuscript revision

1. Confirm the manuscript's protocol, cutoff, selected-study identities and evidence. Preserve the distinction between historical studies, recent inclusions, incomplete assessments and contextual references.
2. Update the corresponding source extraction and bibliography files under `data/sources/`. Keep primary-text attribution, evaluation boundaries, native query references and explicit pending statuses. Do not infer new inclusions from citations or automated duplicate matches.
3. Reconcile source observations, eligibility notes and retrieval status. The ancillary eligibility record contains 38 inclusions and five separate exploratory exclusions. The master original observation set remains 50 records: 38 included, one pending, three excluded and eight other dispositions. Additional retrieval has its own counts and candidate metadata. Do not equate unassessed retrieval records with included studies.
4. Deliberately update `data/source-snapshot.json`: artifact date/title, manuscript fingerprint, source fingerprints, counts and canonical dataset fingerprint. The builder derives current totals and dispositions from the extraction and query records, while preserving the 98 historical count and requiring the original eight update keys to remain included. Deliberately update snapshot expectations and the dated coverage description together with the manuscript; do not introduce unrelated fixed totals in code. Do not simply change hashes to suppress unexplained differences.
5. Preserve the original historical CSV fingerprints. New raw exports belong in a separate dated location, with documented provenance; replacing the old files would destroy the distinction between retrieval rounds.
6. Update the README, protocol and dictionary where the evidence or schema changed, rebuild, run the checks and regression tests, and review the diff. New findings must not be inferred from successful serialization.

The manuscript lives at `publications/survey-atualizar` in the thesis repository; the public companion repository is [rodrigodg1/blockchain-survey](https://github.com/rodrigodg1/blockchain-survey).

The recent source extraction has 15 fields. `source_table` was added to identify the specific manuscript table for every recent record, across the six application-table parts. When tables move or split, run the manuscript exporter to derive these labels before importing the new snapshot. Preserve original extraction fields; a provenance-field addition does not constitute new study evidence or change the normalized dataset schema.

Keep the synthesis matrix, method, contextual evidence and follow-up assessment records with the source snapshot when they support the current manuscript. The current 67-record synthesis matrix is a bounded evidence audit, not uniform coding of all 136 applications. Do not turn a newly cited contextual source, conceptual proposal, formative survey or verified proof relation into an additional inclusion or stronger evaluation claim without the documented source assessment. Version-identified preprints and commentary containing an original workflow must retain their genre and version qualifiers.

`manuscript_sha256` identifies the source manuscript snapshot. The manuscript is not included in this data repository, so this fingerprint documents provenance but cannot establish that an external manuscript remains unchanged. Source and dataset fingerprints are checked locally. The full bibliography includes contextual sources; only the selected study keys determine `application-references.bib` and the dataset.

Annual summaries expose both `extraction_year` and `bibliography_year`. Filter to one basis for analysis. Version-year corrections do not turn a historical study into a recent inclusion.
