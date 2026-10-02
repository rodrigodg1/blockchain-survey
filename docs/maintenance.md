# Maintaining the documented snapshot

The 2 October 2026 snapshot contains **136 included works** (46 privacy, 58 consent and 32 identity), including **50 detailed-comparison examples**. The synthesis matrix adds 17 contextual sources outside the included-work total. Six privacy evaluation summaries repeat included works. Additional retrieval and unfinished candidate screening remain separate from all these counts.

## Rebuilding unchanged inputs

Run `python3 run.py`, followed by `python3 run.py --check`. Both validate source fingerprints, included identities and detailed/context membership before accepting outputs. The check compares every generated file with its in-memory reconstruction. Manifest paths use `/` on every operating system.

The seven generated files are `survey-dataset.csv`, `study-counts.csv`, `search-decision-counts.csv`, `counts.json`, `application-references.bib`, `studies-by-year.csv` and `manifest.json`, all under `data/`. Do not edit them manually.

## Incorporating a manuscript revision

1. Verify the manuscript's included-work identities, search-topic groups and Appendix A table labels. Separately identify detailed examples, contextual sources and repeated evaluation entries. Do not treat every bibliography citation or retrieved candidate as an included work.
2. Update the extraction and bibliography under `data/sources/` only where the evidence changed. Retain source locations, versions, access limits, native query references and pending statuses. A new citation or automated duplicate match does not establish eligibility.
3. Update `data/sources/revisao/manuscript-membership.json` from the manuscript's work tables and stated evidence sets. Record the SHA-256 of the exact manuscript source. Preserve identity-level correspondence; matching totals alone is insufficient.
4. Reconcile search observations, eligibility notes and retrieval status separately. The current original observation set contains 50 records: 38 included, one pending, three excluded and eight other dispositions. The five exploratory exclusions in the ancillary eligibility record and the additional candidate exports have separate provenance and denominators.
5. Deliberately update `data/source-snapshot.json`: dated description, manuscript fingerprint, source fingerprints, expected counts and canonical dataset fingerprint. Its manuscript fingerprint must match the membership record. Preserve historical CSV fingerprints. Investigate changes before accepting new fingerprints; do not change hashes merely to silence a mismatch.
6. Keep the matrix, codebook, compact comparisons and requirement derivations aligned with the retained evidence. Contextual sources remain outside application denominators. Proposed behavior, source-reported measurements, source-access limits and derived assessment questions must remain distinct.
7. Update documentation where the evidence or exported schema changed. Rebuild, run `--check` and `python3 -m unittest discover -s tests -v`, then inspect the diff. Verify that unrelated historical records were preserved.

The manuscript is not distributed in this dataset repository. `manuscript_sha256` and the membership record identify the reconciled snapshot; local checks cannot establish whether an external manuscript subsequently changed. Re-extract membership and recompute its fingerprint whenever a manuscript revision affects the recorded evidence sets.

The recent extraction has 15 fields. Its `source_table` field identifies one of the six Appendix A work-table parts; update labels when those tables move or split. A provenance-field correction does not create new study evidence or change the normalized CSV schema.

Keep genre and version qualifiers for conceptual proposals, formative surveys, preprints and commentary containing an original workflow. Full-text access is not independent reproduction. The 67-row matrix is a selected qualitative comparison, not uniform coding of all 136 works.

Annual summaries expose both `extraction_year` and `bibliography_year`. Use one basis per analysis. Publication-version corrections do not create new inclusions. The full bibliography includes contextual references; included study keys alone determine `application-references.bib` and the normalized dataset.
