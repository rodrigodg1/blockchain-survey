# Survey dataset: blockchain-assisted data sharing

Dataset and source records for **Governance of Blockchain-Assisted Data Sharing: A Survey of Privacy, Consent, and Self-Sovereign Identity**.

Snapshot: **2 October 2026**, with a **30 September 2026 publication cutoff**. The survey is a structured qualitative survey. It does not claim exhaustive retrieval or a systematic review.

## Included works

[data/survey-dataset.csv](data/survey-dataset.csv) contains **136 included studies and proposals**, with one row per work.

| Search-topic group | Included works | Detailed-comparison examples |
|---|---:|---:|
| Privacy | 46 | 12 |
| Consent and permission | 58 | 27 |
| Identity | 32 | 11 |
| **Total** | **136** | **50** |

The groups follow the recorded extraction or retrieval-query family; they are not exclusive categories of technical capabilities. The 136 works comprise 98 initial records and 38 additions. The detailed comparison uses 50 of these works. The remaining 86 were not uniformly assessed against the survey's eight design requirements.

The [synthesis matrix](data/sources/revisao/synthesis-evidence-matrix.csv) contains those **50 examples and 17 contextual sources**, for 67 rows. Contextual theory, specifications and legal guidance are excluded from the 136-work total. The six privacy evaluation summaries in the manuscript refer to already included works and add no studies. Essential methods, comparisons and limitations are presented in the manuscript; this repository records their dataset provenance.

[manuscript-membership.json](data/sources/revisao/manuscript-membership.json) records the identifiers and Appendix A table labels extracted from the dated manuscript, including its detailed examples, contextual sources and privacy evaluation entries. Validation compares these identities with the exported dataset and matrix. The manuscript fingerprint identifies the reconciled version; validation cannot detect changes to a manuscript held outside this repository.

## Evidence and extraction

The survey compares protection targets and constructions (RQ1), authorization and enforcement (RQ2), and checked relations and evaluation evidence (RQ3). The [codebook](data/sources/revisao/synthesis-codebook.md), [requirement derivations](data/sources/revisao/requirement-derivation.csv) and [compact comparisons](data/sources/revisao/rq-application-comparisons.csv) document the analytical attributes and their source locations.

Among the 50 examples, 35 have direct full-text checks, nine use source-specific full-text assessments and six retain more limited evidence. Access status is recorded per source. A described control, a reported evaluation and a derived assessment question remain distinct; inclusion does not establish deployment, regulatory compliance or every claimed security property. Historical evaluation fields were not extracted uniformly. Empty cells mean unextracted information, not absence of an evaluation or limitation.

The original update assessment covers 50 Google Scholar observations: 38 included, one pending primary text, three excluded for scope and eight other dispositions. These 50 search observations are different from the 50 detailed-comparison examples. Additional retrieval contains 843 raw observations and 817 provisionally consolidated candidates; their scientific screening and complete Scholar pagination remain unfinished. They add no works to the included dataset. See [docs/protocol.md](docs/protocol.md) for exact queries, dates and limitations.

## Files

| File | Purpose |
|---|---|
| [data/survey-dataset.csv](data/survey-dataset.csv) | One row per included work, with metadata, provenance and evidence limits |
| [data/counts.json](data/counts.json), [data/study-counts.csv](data/study-counts.csv) | Included-work counts and detailed-comparison counts, with their interpretation limits |
| [data/search-decision-counts.csv](data/search-decision-counts.csv) | Dispositions of the original 50 update observations |
| [data/studies-by-year.csv](data/studies-by-year.csv) | Annual counts by extraction year and bibliography year |
| [data/application-references.bib](data/application-references.bib) | Bibliography of the 136 included works |
| [data/sources/](data/sources/) | Extractions, assessments, search records, synthesis evidence and manuscript bibliography |
| [docs/data-dictionary.json](docs/data-dictionary.json) | Exported fields and missing-value definitions |
| [data/source-snapshot.json](data/source-snapshot.json) | Manuscript and input fingerprints, expected counts and preserved historical-file fingerprints |
| [data/manifest.json](data/manifest.json) | Build-input and generated-output SHA-256 fingerprints |

`source_extraction_file` resolves relative to `data/sources/`. `source_record_number` is a one-based CSV data-record index excluding the header, not a physical line number. `source_table` identifies the Appendix A work table. Source URLs and section/page locations identify examined passages; article full texts and indexed abstracts are not redistributed.

The complete manuscript bibliography includes contextual and background references. Its entry count is not the number of included works. Fields ending in `_bibtex` retain BibTeX braces and escapes; some extraction fields retain LaTeX notation. Internal `historical` and `supplementary_update` values preserve extraction provenance, not separate submission documents or evidence-quality classes.

## Reproduce and validate

Requires **Python 3.9 or newer**, with no third-party packages, network access, external repository or LaTeX installation.

```sh
python3 run.py --check
python3 run.py
python3 run.py --check
python3 -m unittest discover -s tests -v
```

`--check` verifies fingerprints, study identities, group and table assignments, detailed/context membership, counts, decisions and generated outputs without rewriting data. Running without `--check` rebuilds the seven generated files under `data/` after validation. Neither command searches, screens additional candidates or changes historical CSVs. Paths resolve from the scripts and manifest paths use `/` across platforms.

These checks establish consistency of the recorded dataset. They do not independently validate source interpretations, reproduce reviewed systems or establish exhaustive coverage.

## Historical records and maintenance

The existing `privacy/`, `consent/`, `identity/` and `total_works_by_year.csv` files are preserved unchanged as historical retrieval/processing records. They are not the current included-work dataset. The retained `analysis-expansion-*` and earlier revision records describe dated preparation stages, not the current manuscript or current RQs. Read [docs/legacy-data.md](docs/legacy-data.md) before using them. The old federated-learning description is not an additional search family; `identity/fl_merged_dataset.csv` retains its historical filename.

`process-papers.py` performs a read-only duplicate audit. Missing DOIs are never grouped as a shared identifier, and conflicting DOI/title matches remain candidates for review:

```sh
python3 process-papers.py > /tmp/blockchain-survey-legacy-audit.json
```

Do not edit generated files to force a total. Reconcile study identities with the manuscript, update source records and snapshot expectations deliberately, then rebuild and check. See [docs/maintenance.md](docs/maintenance.md).

The repository retains its [Apache 2.0 license](LICENSE). Bibliographic descriptions and links do not transfer rights to the cited publications.
