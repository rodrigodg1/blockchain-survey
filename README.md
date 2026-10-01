# Governance of Blockchain-Assisted Data Sharing

Companion data for **Governance of Blockchain-Assisted Data Sharing: A Survey of Privacy, Consent, and Self-Sovereign Identity**.

**Public survey data repository:** [https://github.com/rodrigodg1/blockchain-survey](https://github.com/rodrigodg1/blockchain-survey).

**Current manuscript workspace:** `publications/survey-atualizar` in [the thesis repository](https://github.com/rodrigodg1/phd-thesis), with `main.tex` as the canonical manuscript source. The manuscript is developed within the thesis repository; this companion repository distributes its documented data, source records and portable validation scripts.

Updated on **1 October 2026** to match the revised manuscript. The survey is a **structured qualitative survey**. It examines decision authority, confidentiality, consent, identity, access enforcement, and accountability in blockchain-assisted data sharing. It does not claim an exhaustive systematic review or PRISMA compliance.

The current manuscript relates sharing and processing operations to the actors who authorize, execute, release and review information. Eight requirements (G1–G8) separate identity/authority, authorization scope/state, custody/release, confidentiality/correctness, audit/accountability, withdrawal/status, output inference, and provenance/truth. The 67-record synthesis matrix covers 50 application examples and 17 contextual sources. It is a bounded evidence audit, not uniform coding of all 136 records or validation of a reference architecture. The [alignment evidence](data/sources/revisao/thesis-alignment-evidence.md) distinguishes credential and record checks from specific computation relations, records conditional links to private QoE analytics, and compares the contribution with existing data-sovereignty work. The application selection and counts are unchanged.

## Current application-study collection

Use [data/survey-dataset.csv](data/survey-dataset.csv), not the historical merged search exports.

| Accounting group | Historical | Supplementary update | Combined |
|---|---:|---:|---:|
| Privacy | 40 | 6 | 46 |
| Consent | 33 | 25 | 58 |
| Identity | 25 | 7 | 32 |
| **Total** | **98** | **38** | **136** |

These groups track the historical extraction or the query family that retrieved a recent study. They are not mutually exclusive categories of system capabilities. Related surveys, standards, regulations, and platform documentation are contextual sources and are excluded from the 136 application records.

Searches used the original title predicates, a 2024--2026 filter and a **30 September 2026 publication cutoff**. The preserved original 50-record Scholar observation set now contains **38 included, one pending, three excluded and eight other dispositions**. Of the 18 observations still unresolved after the first assessment, 14 were included after reading primary methods, two were excluded for application scope, one was identified as a review and one still requires primary text. Pending access is not an exclusion. The application collection contains 136 studies and proposals, with evidence limits recorded per recent study.

Scopus queries S02/S05/S08 were executed on **1 October 2026** and all **496/47/175 observations** were exported. ACM queries S03/S06/S09 returned **15/12/8 observations** from the **Full-Text Collection**, using January 2024 through September 2026. ACM's Guide to Computing Literature was not searched. Expanded Scholar S01 pages **19--27** are retained (90 observations). Other expanded pages are not claimed as preserved results.

The additional retrieval contains **843 raw observations and 817 provisionally consolidated candidate records**. These are separate from the 136 included applications. Additional-candidate scientific screening and Scholar pagination remain incomplete. Candidate metadata, identifiers and current dispositions are distributed in [search-completion-candidates-metadata.csv](data/sources/revisao/search-completion-candidates-metadata.csv). Indexed abstracts are not redistributed. Raw-file fingerprints and the manuscript fingerprint are recorded in [source-snapshot.json](data/source-snapshot.json).

## Files

| File | Purpose |
|---|---|
| [data/survey-dataset.csv](data/survey-dataset.csv) | One row per included application study, with metadata, provenance and evidence boundaries |
| [data/study-counts.csv](data/study-counts.csv), [data/counts.json](data/counts.json) | Collection counts and the limits of their interpretation |
| [data/search-decision-counts.csv](data/search-decision-counts.csv) | Dispositions of the 50 observed update records |
| [data/studies-by-year.csv](data/studies-by-year.csv) | Annual counts, separately by extraction year and bibliography year |
| [data/application-references.bib](data/application-references.bib) | Bibliographic entries for the 136 application records |
| [data/sources/](data/sources/) | Historical/recent extractions, query and follow-up assessment records, eligibility notes, retrieval status, source-linked synthesis evidence and the manuscript bibliography |
| [docs/data-dictionary.json](docs/data-dictionary.json) | Definition of every exported field and missing-value semantics |
| [data/source-snapshot.json](data/source-snapshot.json) | Source version, manuscript fingerprint, expected collection and preserved historical-file fingerprints |
| [data/manifest.json](data/manifest.json) | SHA-256 fingerprints of build inputs and generated outputs |

`revisao/recent-extraction.csv` in the source snapshot has 15 fields: the 13 original mechanism/evidence fields plus `verified_publication_title` and the additive `source_table` provenance field. `source_table` identifies the specific manuscript comparison table, across the privacy, consent and identity application tables. This addition does not change study identity or the normalized dataset schema.

`source_extraction_file` resolves relative to **data/sources/**. `source_record_number` is a one-based CSV data-record index, excluding the header; it is not a physical line number. Primary-text URLs and section/page locations are recorded for the recent studies. Article full texts are not redistributed here.

The bibliography under `data/sources/` includes contextual citations. Its entry count is not the number of included studies. Fields ending in `_bibtex` retain BibTeX braces and escapes; some extraction fields retain LaTeX notation.

## Reproduce and validate

Requires **Python 3.9 or newer**, with no third-party packages, network access, sibling repository, LaTeX installation, or image tools.

From this repository:

```sh
python3 run.py --check
python3 run.py
python3 run.py --check
python3 -m unittest discover -s tests -v
```

- `--check` verifies the input snapshot, study identities, counts, decisions, source mapping and generated files without rewriting the data files. Python may create its usual ignored bytecode cache.
- Running without `--check` rebuilds the seven generated files directly under `data/`. All input and collection checks complete before writing. It does not rewrite the historical CSVs, perform searches, select additional studies, or generate images.
- Paths are resolved from the scripts, so `python3 /path/to/blockchain-survey/run.py --check` also works from another directory.

The canonical dataset fingerprint and expected collection counts are recorded in [data/source-snapshot.json](data/source-snapshot.json). The builder requires the exported CSV to match that deliberately synchronized manuscript snapshot; the fingerprint is kept there rather than duplicated in this README.

Included records encompass implemented systems, conceptual designs, version-identified preprints and a commentary containing an original proposed workflow. Their genres and evaluation limits are recorded explicitly. Inclusion does not establish implementation, publication acceptance, secure deployment or regulatory compliance.

These checks establish artifact consistency. They do not establish exhaustive coverage, independent scientific validation, regulatory compliance, or reproducibility of the reviewed implementations.

## Method and historical material

Read [docs/protocol.md](docs/protocol.md) for scope, queries, eligibility, extraction and limitations, and [docs/legacy-data.md](docs/legacy-data.md) for the historical export audit.

The existing `privacy/`, `consent/`, `identity/`, and `total_works_by_year.csv` files are preserved unchanged. They contain historical retrieval/processing records, not the current included-study dataset. The old federated-learning search description is not an additional search family in the current three-topic protocol. The misleading historical filename `identity/fl_merged_dataset.csv` is retained for provenance.

The old `process-papers.py` has been replaced by a **read-only audit**. It identifies candidate duplicate groups without dropping records or overwriting merged exports:

```sh
python3 process-papers.py > /tmp/blockchain-survey-legacy-audit.json
```

The original deduplication treated missing DOIs as duplicates. The replacement never groups empty DOIs as a matching identifier and reports title matches with conflicting DOIs for review. Candidate groups can overlap and are not screening decisions.

## Updating this snapshot

Do not edit generated files to adjust a total. Update the evidence and extraction records first, then deliberately revise the snapshot fingerprints, collection expectations and documented date together with the manuscript. The generator intentionally rejects changes that no longer match this release. See [docs/maintenance.md](docs/maintenance.md).

The repository retains its [Apache 2.0 license](LICENSE). Bibliographic descriptions and links do not transfer rights to the cited publications.
