# Maintaining the documented snapshot

The current release is tied to the manuscript and extraction state of 1 October 2026: 122 application records, comprising 98 historical and 24 update records. The update includes 16 additions from follow-up assessment of 35 previously pending observations; the original 50-record retrieval denominator and eight update inclusions are preserved. The builder is intentionally a reproducible exporter of that documented selection, not a crawler or an automatic screening tool.

## Rebuilding unchanged inputs

Run `python3 run.py`, followed by `python3 run.py --check`. Both commands validate the source fingerprints and identities before accepting the exported collection. The check compares every generated file with its in-memory reconstruction and fails on missing, modified or stale output. The output manifest records the generator, dictionary, source inputs and preserved historical CSVs.

The seven generated files are `survey-dataset.csv`, `study-counts.csv`, `search-decision-counts.csv`, `counts.json`, `application-references.bib`, `studies-by-year.csv` and `manifest.json`, all under `data/`. Do not edit them manually.

## Incorporating a subsequent manuscript revision

1. Confirm the manuscript's protocol, cutoff, selected-study identities and evidence. Preserve the distinction between historical studies, recent inclusions, incomplete assessments and contextual references.
2. Update the corresponding source extraction and bibliography files under `data/sources/`. Keep primary-text attribution, evaluation boundaries, native query references and explicit pending statuses. Do not infer new inclusions from citations or automated duplicate matches.
3. Reconcile query observations, eligibility notes and the retrieval-status summary. Their roles differ: the 29-row eligibility file contains 24 inclusions and five prior exploratory title-predicate exclusions; it is not the master decision log for the 50 observed results. The 35-row follow-up assessment log records the disposition changes producing 24 included, 18 pending, one excluded and seven other dispositions across those 50 observations. Keep prior decisions and examined version metadata.
4. Deliberately update `data/source-snapshot.json`: artifact date/title, manuscript fingerprint, source fingerprints, counts and canonical dataset fingerprint. The builder derives current totals and dispositions from the extraction and query records, while preserving the 98 historical count and requiring the original eight update keys to remain included. Deliberately update snapshot expectations and the dated coverage description together with the manuscript; do not introduce unrelated fixed totals in code. Do not simply change hashes to suppress unexplained differences.
5. Preserve the original historical CSV fingerprints. New raw exports belong in a separate dated location, with documented provenance; replacing the old files would destroy the distinction between retrieval rounds.
6. Update the README, protocol and dictionary where the evidence or schema changed, rebuild, run the checks and regression tests, and review the diff. New findings must not be inferred from successful serialization.

The manuscript lives at `/Users/rodrigodgarcia/Desktop/phd-thesis/publications/survey-atualizar`; the public companion repository is [rodrigodg1/blockchain-survey](https://github.com/rodrigodg1/blockchain-survey).

The recent source extraction has 15 fields. `source_table` was added to identify the specific manuscript table for every recent record, including the three supplementary table parts. When tables move or split, run the manuscript exporter to derive these labels before importing the new snapshot. Preserve original extraction fields; a provenance-field addition does not constitute new study evidence or change the normalized dataset schema.

Keep the synthesis matrix, method, contextual evidence and follow-up assessment records with the source snapshot when they support the current manuscript. The current 53-record synthesis matrix is a bounded evidence audit, not uniform coding of all 122 applications. Do not turn a newly cited contextual source, conceptual proposal, formative survey or verified proof relation into an additional inclusion or stronger evaluation claim without the documented source assessment. Version-identified preprints and commentary containing an original workflow must retain their genre and version qualifiers.

`manuscript_sha256` identifies the source manuscript snapshot. The manuscript is not included in this data repository, so this fingerprint documents provenance but cannot establish that an external manuscript remains unchanged. Source and dataset fingerprints are checked locally. The full bibliography includes contextual sources; only the selected study keys determine `application-references.bib` and the dataset.

Annual summaries expose both `extraction_year` and `bibliography_year`. Filter to one basis for analysis. Version-year corrections do not turn a historical study into a recent inclusion.
