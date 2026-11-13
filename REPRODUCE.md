# Reproduce the dataset, comparisons, and figures

These commands reconstruct the retained collection and its descriptive results. They do not rerun the reviewed systems, repeat literature screening, or recover undocumented selection decisions.

## Requirements

| Task | Requirement | Version command |
|---|---|---|
| Obtain the repository | Git | `git --version` |
| Dataset, comparisons, and source validation | Python 3.9 or newer; standard library | `python3 --version` |
| Plotting | Python 3.14 and `requirements-plots.txt` | `python3 --version` |

The plotting commands were executed with Python 3.14.5 and the pinned dependencies. Use a Python 3.14 interpreter when creating the plotting environment. On Windows, replace `.venv/bin/python` with `.venv\Scripts\python.exe`.

```sh
git clone https://github.com/rodrigodg1/blockchain-survey.git
cd blockchain-survey
```

## 1. Rebuild and validate the data

```sh
python3 run.py
python3 run.py --validate
python3 verify_source.py
python3 -m unittest discover -s tests -v
```

`run.py` validates source fingerprints, publication identities, table assignments, separate retrieval strata, detailed comparisons, and evaluation records before writing outputs. `--validate` reconstructs the expected outputs in memory and compares them with the retained files without rewriting them.

Nine generated files appear under `data/`:

| File | Contents |
|---|---|
| `survey-dataset.csv` | 139 included publications and their extraction fields |
| `application-summaries.csv` | 139 application and approach descriptions |
| `platform-comparisons.json` | 19 privacy systems and six identity components, with reference URLs |
| `study-counts.csv` | Historical, supplementary, and combined group totals |
| `search-decision-counts.csv` | Decisions for the original 50 Scholar observations |
| `counts.json` | Collection totals, retrieval strata, evaluation records, and limits |
| `application-references.bib` | Bibliographic entries for the included publications |
| `studies-by-year.csv` | Separate annual totals by extraction year and bibliography year |
| `manifest.json` | Input and generated-file SHA-256 fingerprints |

Expected group totals are **48 privacy, 59 consent, and 32 identity**. Detailed comparisons contain 53 included publications and 17 contextual sources. Evaluation extraction contains 8/26/7 records; the retained synthesis excerpts present 7/26/7. These are different presentation scopes, not different included-publication totals.

`verify_source.py` validates the retained inventory and comparison excerpts. It supports prose-based privacy synthesis and table-based consent and identity evaluations. All inputs required for its default command are included in this repository.

## 2. Generate and validate the chronology

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-plots.txt
.venv/bin/python reproduce_plots.py
.venv/bin/python reproduce_plots.py --validate
```

The plotter stages its inputs in a temporary directory, validates the dataset, and compares all five regenerated timeline CSVs with the retained numerical records and source descriptions. It writes `technology-timeline.pdf`, `technology-timeline.png`, and `manifest.json` under `data/figures/`.

`--validate` also verifies the retained figure files against their recorded hashes. In the recorded rendering environment, regenerated figures must match byte for byte. Another Python, package, or operating-system environment may produce different binary figures. The result then reports `different_rendering_environment`; numerical records must still match exactly. Altered retained figures or numerical differences always fail validation.

For a separate output location:

```sh
.venv/bin/python reproduce_plots.py --output-dir output/figures
.venv/bin/python reproduce_plots.py --validate --output-dir output/figures
```

The chronology uses all 139 publications. Its period denominators are 5, 29, 62, and 43. A total of 62 publications name at least one selected approach. No random sampling, iteration count, or performance experiment is involved.

## 3. Optional historical illustration

The retained processing-cost illustration describes two studies with different tasks and conditions. It does not support a collection-wide performance comparison.

```sh
.venv/bin/python reproduce_plots.py --include-legacy --output-dir output/legacy-figures
.venv/bin/python reproduce_plots.py --validate --include-legacy --output-dir output/legacy-figures
```

A separate destination is required. These commands generate the chronology plus the historical illustration without replacing the current figure manifest.

## 4. Inspect historical retrieval records

```sh
python3 process-papers.py
```

The command reads nine historical source exports and prints candidate duplicate groups as JSON. It does not delete, merge, or select records. Missing DOI values never form a DOI-based match. Candidate groups can overlap, so their counts cannot be subtracted to infer a selected-study total.

[Protocol and limitations](docs/protocol.md), [field definitions](docs/data-dictionary.json), and [maintenance instructions](docs/maintenance.md) provide the interpretation and update rules.
