# Reproduce the survey data and current plots

This procedure rebuilds the retained dataset, descriptive counts and the current chronology figure. It does not rerun reviewed systems, repeat literature screening or recover undocumented historical decisions.

## Prerequisites

| Task | Requirement | Check |
|---|---|---|
| Obtain the public snapshot | Git | `git --version` |
| Dataset and manuscript checks | Python 3.9+; standard library | `python3 --version` |
| Current plots | Tested with Python 3.14.7 and pinned packages | `python3 --version`; `.venv/bin/python -m pip check` |

```sh
git clone https://github.com/rodrigodg1/blockchain-survey.git
cd blockchain-survey
```

## 1. Rebuild and check the dataset

```sh
python3 run.py
python3 run.py --check
python3 -m unittest discover -s tests -v
```

The existing `run.py` calls `scripts/build_dataset.py`. It checks source and historical-file fingerprints, reconstructs 139 publications from their extraction/bibliography records, checks exact manuscript membership, and verifies separate search strata. It also checks the 53 detailed applications, 17 contextual sources, evaluation-table memberships and recorded objective citations before accepting outputs.

Outputs under `data/`: `survey-dataset.csv`, `study-counts.csv`, `search-decision-counts.csv`, `counts.json`, `application-references.bib`, `studies-by-year.csv` and `manifest.json`. Rebuilding unchanged inputs must leave these files unchanged. `--check` compares without repairing or rewriting files.

Expected totals: 48 privacy, 59 consent, 32 identity; 139 unique included publications; 53 detailed applications; 46 direct or assessment-stage full-text records and seven limited records. The 38 original Scholar inclusions, two additional Scopus inclusions and one targeted S04 inclusion remain separate from the 98 historical records. The 777 pending additional candidates remain pending.

## 2. Reproduce the current chronology plot

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-plots.txt
.venv/bin/python -m pip check
.venv/bin/python reproduce_plots.py
.venv/bin/python reproduce_plots.py --check
```

On Windows, use `.venv\Scripts\python.exe` instead of `.venv/bin/python`.

The wrapper `reproduce_plots.py` calls `scripts/reproduce_plots.py`. It validates the published dataset, stages the original script and its input layout in a temporary directory, and runs:

- `data/sources/revisao/plot_technology_timeline.py`: publication-window counts, plotted percentages and trace records.

All five regenerated timeline CSVs are compared with the published records before output. The six-table inventory excerpt supplies the same application/control descriptions used by the manuscript generator; the complete manuscript and third-party full texts are not needed.

Outputs under `data/figures/`:

- `technology-timeline.pdf` and `.png`.
- `manifest.json`, recording input hashes, rendering versions and output hashes.

Use `--output-dir /path/to/plots` for another destination. `--check` regenerates in isolation and compares without writing. The pinned environment reproduces the current chronology PDF byte for byte. Different rendering environments can change binary output; the recorded numerical data and trace-table checks define the scientific correspondence.

No sampling or repetition parameter applies. The current plot uses all 139 included publications. The original plotting scripts and their settings are preserved. No plotting function or existing dataset command was removed.

## Optional reproduction of the excluded illustration

The earlier PrivDA/Kang processing-cost illustration is excluded from the current manuscript. It describes two studies with different tasks and conditions, not survey-wide comparative performance. Its generator, input values and output files remain available for historical inspection.

```sh
.venv/bin/python reproduce_plots.py --include-legacy --output-dir /tmp/survey-legacy-plots
```

This optional command also runs the unchanged `plot_processing_costs.py`. A separate destination is required to keep the current-output manifest unchanged. The default command produces only the chronology plot.

## 3. Verify the manuscript used with this snapshot

When the external manuscript source is available:

```sh
python3 verify_manuscript.py /path/to/main.tex
```

This checks the complete source SHA-256, all 139 inventory identities and table assignments, the detailed markers, evaluation memberships, RQs, objective citations, current plot membership and inventory descriptions. A later editorial change produces a source mismatch and requires reconciliation through [docs/maintenance.md](docs/maintenance.md).

## Other retained records

`python3 process-papers.py` audits historical duplicate candidates without deleting or merging records. Historical retrieval files are preserved; their output counts are not the current included-publication total.

[docs/protocol.md](docs/protocol.md) records queries, access limits and unfinished screening. Source hashes establish correspondence and detect drift; they do not certify source interpretation, completeness, security or legal compliance.
