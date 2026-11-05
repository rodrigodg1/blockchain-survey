# Blockchain-Aided Data Sharing: Dataset and Analyses of Privacy, Consent, and Identity Management

Dataset, evidence records and plotting scripts supporting the survey on privacy, consent, and identity management in blockchain-aided data sharing.

Snapshot: **4 November 2026**. Publication cutoff: **30 September 2026**. This is a qualitative survey with selective retrieval and incomplete candidate screening.

## Manuscript correspondence

[data/survey-dataset.csv](data/survey-dataset.csv) contains one row per included publication. Each publication belongs to one search-topic group for counting; its controls can address multiple topics.

| Search-topic group | Included publications | Detailed comparisons | Evaluation/limits entries |
|---|---:|---:|---:|
| Privacy | 48 | 14 | 8 |
| Consent and permission | 59 | 28 | 26 |
| Decentralized identity | 32 | 11 | 7 |
| **Total** | **139** | **53** | **41** |

The evaluation entries repeat included publications and add no studies. The [70-row synthesis matrix](data/sources/revisao/synthesis-evidence-matrix.csv) contains the 53 detailed applications and 17 contextual sources. The other 86 included publications were not uniformly examined against the eight evaluation objectives. Source records distinguish 37 direct full-text checks, nine assessment-stage full-text checks and seven limited or unverified application sources. These are recorded access levels, not independent replication.

The 139 publications comprise 98 retained historical records and 41 additions: 38 from the original 50 Scholar observations, two from additional Scopus exports and one targeted S04 follow-up. The 817 additional consolidated candidates include 777 awaiting title/abstract screening. Retrieval does not establish eligibility. [Protocol, exact queries and limitations](docs/protocol.md).

The manuscript RQs are:

1. What mechanisms or strategies are used in blockchain applications to ensure privacy, consent management, and selective sharing among multiple stakeholders?
2. How can individuals control their identity in a decentralized infrastructure?
3. What are the existing blockchain platforms and protocols enabling user privacy and identity management?

[Manuscript membership](data/sources/revisao/manuscript-membership.json) records the included identities, six inventory-table assignments, detailed application identities from the synthesis matrix, three evaluation-table memberships, RQs and objective citations. [Source snapshot](data/source-snapshot.json) records the exact manuscript source SHA-256. The complete manuscript is not redistributed; its [application-inventory excerpt](data/sources/revisao/manuscript-inventory.tex) supplies the original timeline generator.

## Reproduce

The dataset needs Python 3.9 or newer and its standard library. Run from this repository:

```sh
python3 run.py --check
python3 run.py
python3 -m unittest discover -s tests -v
```

The current quantitative figure uses the manuscript's unchanged chronology script:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-plots.txt
.venv/bin/python reproduce_plots.py
.venv/bin/python reproduce_plots.py --check
```

The plotting environment was checked with Python 3.14.7 and the pinned packages. The generated chronology PDF matches the current manuscript figure byte for byte in that environment. [REPRODUCE.md](REPRODUCE.md) documents prerequisites, outputs, manuscript verification and the scope of these checks.

| Figure status | Original generator | Retained PDF |
|---|---|---|
| Current: reported approaches over publication windows | [plot_technology_timeline.py](data/sources/revisao/plot_technology_timeline.py) | [technology-timeline.pdf](data/figures/technology-timeline.pdf) |
| Excluded: earlier two-study illustration (PrivDA/Kang) | [plot_processing_costs.py](data/sources/revisao/plot_processing_costs.py) | [synthesis-processing-costs.pdf](data/figures/synthesis-processing-costs.pdf) |

The timeline uses all 139 publications as denominators: 5, 29, 62 and 43 per publication window. Sixty-one name at least one plotted approach. The excluded processing-cost illustration uses only two studies and does not synthesize survey-wide performance. Its retained values and measurement limits are in [processing-costs-data.json](data/sources/revisao/processing-costs-data.json). Its original generator remains available through the optional legacy command in `REPRODUCE.md`; it is not run by default.

## Data and provenance

- [counts.json](data/counts.json), [study-counts.csv](data/study-counts.csv) and [studies-by-year.csv](data/studies-by-year.csv): regenerated totals, detailed membership and date bases.
- [application-references.bib](data/application-references.bib): the 139 included publications. The full source bibliography also contains background and contextual references.
- [data/sources/](data/sources/): extractions, source locations, search decisions, access limits, coding rules and objective derivations.
- [data/manifest.json](data/manifest.json): source and generated-data fingerprints. [Figure manifest](data/figures/manifest.json): current plotting inputs, environment and output fingerprints. [Figure status](data/figures/README.md) distinguishes the current plot from the excluded illustration.
- [Data dictionary](docs/data-dictionary.json) and [maintenance procedure](docs/maintenance.md).

Empty extraction fields mean unextracted information. Full-text access does not establish correct interpretation, security, deployment, regulatory compliance or independent reproduction. No exhaustive retrieval, independent human double screening, inter-rater agreement or pooled performance ranking is claimed.

Historical `privacy/`, `consent/`, `identity/` and `total_works_by_year.csv` remain unchanged. They are not the current included-publication dataset. [Legacy-data limitations](docs/legacy-data.md) explain the historical missing-DOI processing problem. `process-papers.py` provides a read-only audit and does not discard DOI-less records.

The repository retains its [Apache 2.0 license](LICENSE). Bibliographic descriptions and links do not transfer rights to the cited publications; article full texts and indexed abstracts are not redistributed.
