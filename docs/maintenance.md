# Maintaining correspondence with the manuscript

The 4 November 2026 snapshot contains 139 publications (48/59/32), 53 detailed application examples, 17 contextual sources, and evaluation-table memberships of 8/26/7. The original 50 Scholar observations, 817 additional candidates and one targeted follow-up retain separate provenance and denominators.

## Rebuild unchanged inputs

Run `python3 run.py`, then `python3 run.py --check` and the tests in `REPRODUCE.md`. The seven generated dataset files must match their reconstruction. Historical retrieval CSVs remain fingerprinted and unchanged. Do not edit generated totals manually.

## Incorporate a manuscript revision

1. Verify the external manuscript with `python3 verify_manuscript.py /path/to/main.tex`. A different source SHA-256 requires deliberate reconciliation, even when totals match.
2. Extract the six inventory memberships, detailed dagger markers, three evaluation-table memberships, RQs and objective citations. Update `data/sources/revisao/manuscript-membership.json` from those identities, not from bibliography size. Preserve the exact application-inventory excerpt used by the timeline plotter.
3. Update source extractions and bibliography only where recorded evidence changed. Retain primary locations, versions, access limits and native query identifiers. New candidate retrieval alone does not establish inclusion. Source text must use LF newlines, as specified in `.gitattributes`, before fingerprinting.
4. Reconcile the original Scholar, additional-export and targeted-follow-up decisions separately. Retain pending decisions and do not treat duplicate candidate matches as new studies. Public candidate metadata excludes indexed abstracts.
5. Keep the matrix, codebook, compact comparisons, objective derivations and source-access records aligned. Contextual sources stay outside application counts. Proposed behavior, reported measurements and analytical objectives remain distinct.
6. Deliberately update `data/source-snapshot.json`: date, exact title, manuscript fingerprint, source fingerprints, expected counts and canonical dataset fingerprint. Investigate every changed source. Historical CSV fingerprints must remain unchanged unless their preservation task is explicitly reopened.
7. Rebuild data, run checks and tests, regenerate plots with the unchanged scientific input values, and verify the external manuscript again. Changes to original plot scripts or input descriptions must be reviewed as code or evidence changes, not accepted solely by replacing output hashes.
8. Inspect the diff, including the README and protocol. Publish the synchronized snapshot and verify it from a fresh clone.

The complete manuscript is not distributed here. The membership record and inventory excerpt support identity and plotting checks; the source SHA-256 identifies the exact external manuscript. `verify_manuscript.py` compares the local manuscript when it is available. Repository-only checks cannot detect a later external edit without that file.

`source_table` records Section 5 inventory labels. Historical `Appendix A` wording in dated preparation records belongs to older manuscript structure. Dated historical snapshots retain their original counts and are not assertions about the current collection.

The plotting wrapper stages the existing plotters' original directory layout in a temporary directory. The original plotters remain available under `data/sources/revisao/`. Their regenerated trace tables are checked before figure outputs are written. No iteration or sample-size knob applies to these deterministic descriptions of the fixed survey collection.
