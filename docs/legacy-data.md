# Historical export preservation and processing correction

The CSV files that existed before this update are preserved byte-for-byte. Their hashes and the original checkout commit are recorded in [source-snapshot.json](../data/source-snapshot.json). The new generator checks those hashes and writes only the current generated files under `data/`.

## Available exports versus former figure

| Family | Google CSV | Scopus CSV | ACM CSV | CSV concatenation | Former figure concatenation | Historical selected studies |
|---|---:|---:|---:|---:|---:|---:|
| Privacy | 674 | 394 | 21 | 1089 | 1107 | 40 |
| Consent | 154 | 88 | 45 | 287 | 297 | 33 |
| Identity | 148 | 104 | 6 | 258 | 319 | 25 |

The former figure used ACM privacy = 39, Google consent = 164 and Google identity = 209. Available records do not establish why those figures differ. Neither set is a new retrieval count for the updated survey.

The retained merged exports contain 411 privacy, 126 consent and 108 identity records. They are search-processing outputs, not the selected-study collection. `identity/fl_merged_dataset.csv` retains its historical filename but contains the identity merge. `privacy/merged.csv` is empty. The old `total_works_by_year.csv` contains 2015–2022 counts and includes federated learning; it does not describe the revised 122-record application collection. Use [studies-by-year.csv](../data/studies-by-year.csv), choosing one `year_basis` rather than summing both.

## Historical deduplication defect

The earlier script concatenated Google, Scopus and ACM rows, removed duplicates on DOI, then removed exact-title duplicates. It treated missing DOI as a shared repeated value. The audit of the available exports found:

| Family | Removed in DOI stage | Removed in later title stage | Remaining |
|---|---:|---:|---:|
| Privacy | 668 | 10 | 411 |
| Consent | 159 | 2 | 126 |
| Identity | 149 | 1 | 108 |

The former figure's “Duplicated Total” labels match the DOI-stage removal counts, not unique records remaining. Missing DOI alone is not evidence that two publications are duplicates. The selected historical collection is nevertheless preserved: reconstructing a different historical selection would require evidence not present in these exports. The 1 October follow-up added 16 eligible application records from the previously observed update candidates, producing 98 historical plus 24 recent records. It did not revise the historical selection, any legacy export, or the retrieval counts in the table above. Current combined accounting groups are 44 privacy, 48 consent and 30 identity; these are not reconstructed search totals.

## Current script behavior

`process-papers.py` now delegates to `scripts/audit_legacy_exports.py`. It only reads the nine source exports and writes JSON to standard output. It reports nonempty normalized DOI matches and normalized-title matches with source-file/record provenance. Missing identifiers never form a DOI match; title groups with multiple distinct DOIs are explicitly flagged.

These are candidate matches, not confirmed duplicate publications. DOI and title groups can overlap. No records are removed, no historical files are overwritten, and no corrected historical selection total is inferred. The original scripts remain recoverable from the Git commit recorded in the snapshot.
