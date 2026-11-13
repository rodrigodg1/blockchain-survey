# Blockchain-Aided Data Sharing: Dataset and Analyses of Privacy, Consent, and Identity Management

Data, source records, comparisons, and reproduction scripts for blockchain-aided data sharing. The collection covers privacy, consent and permission management, and decentralized identity.

Snapshot: **13 November 2026**. Retrieval and screening remain incomplete. The [protocol](docs/protocol.md) records the publication cutoff, queries, selection decisions, and coverage limits.

## Explore the collection

| Search-topic group | Included publications | Detailed comparisons | Evaluation records |
|---|---:|---:|---:|
| Privacy | 48 | 14 | 8 |
| Consent and permission | 59 | 28 | 26 |
| Decentralized identity | 32 | 11 | 7 |
| **Total** | **139** | **53** | **41** |

Each publication belongs to one group for counting. Its mechanisms may address more than one topic. Evaluation records describe publications already included in the collection. They do not add studies. The privacy synthesis excerpt discusses seven of the eight retained privacy evaluation records; the InvisiReveal extraction remains available in the dataset.

Start with:

- [Application summaries](data/application-summaries.csv): application and approach descriptions for all 139 publications.
- [Complete dataset](data/survey-dataset.csv): bibliographic identities, extraction fields, evaluation descriptions, source locations, and access limits. [Field definitions](docs/data-dictionary.json).
- [Platform comparisons](data/platform-comparisons.json): 19 privacy systems and six identity components, with their roles, protected information, trust assumptions, limits, and reference URLs.
- [Detailed evidence matrix](data/sources/revisao/synthesis-evidence-matrix.csv): 53 included publications and 17 contextual sources. Contextual sources are excluded from the 139-publication total.
- [Included-publication references](data/application-references.bib), [counts](data/counts.json), and [annual totals](data/studies-by-year.csv).

The 53 detailed publications include 37 with direct full-text assessment, nine with an assessment-stage full-text record, and seven with limited or unverified access. These access levels do not establish independent reproduction or validate security claims. The remaining 86 included publications were not uniformly assessed against the eight evaluation objectives.

## Reproduce the results

Dataset commands use Python 3.9 or newer and its standard library:

```sh
python3 run.py
python3 run.py --validate
python3 verify_source.py
python3 -m unittest discover -s tests -v
```

For figures, use Python 3.14 and the pinned plotting dependencies:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-plots.txt
.venv/bin/python reproduce_plots.py
.venv/bin/python reproduce_plots.py --validate
```

[REPRODUCE.md](REPRODUCE.md) describes prerequisites, output files, validation results, and optional historical reproduction. No external document or third-party full text is required for these commands.

## Recorded approaches across publication periods

![Recorded approaches across publication periods](data/figures/technology-timeline.png)

The four period denominators are **5, 29, 62, and 43**, totaling 139 publications. **62 publications** name at least one of the twelve plotted approaches. The other 77 remain in the denominators. A publication can contribute to several series.

The proxy re-encryption count for 2021–2023 is **4 of 62 publications (6.45%)**. Each plotted value can be traced through the [period counts](data/sources/revisao/technology-timeline-periods.csv), [publication annotations](data/sources/revisao/technology-timeline-records.csv), and [matched descriptions](data/sources/revisao/technology-timeline-matches.csv). The [plot method](data/sources/revisao/technology-timeline-method.md) explains matching rules and interpretation limits.

The figure measures recorded mentions. It does not measure adoption, effectiveness, deployment, or the date a technology was invented. The earlier two-study processing-cost illustration remains available as a historical example and is excluded from the default plotting command.

## Provenance and limitations

The collection contains 98 historical publications and 41 additions: 38 from the original 50 Scholar observations, two from additional Scopus exports, and one targeted S04 follow-up. The 817 additional consolidated candidates include 777 awaiting title/abstract screening. Retrieval alone does not establish inclusion.

[Collection membership](data/sources/revisao/collection-membership.json) records included identities, inventory assignments, evaluation identities, research questions, and objective citations. [Source fingerprints](data/source-snapshot.json) and the [generated-file manifest](data/manifest.json) identify the retained inputs and outputs. Dated evidence records preserve their original scope; their earlier totals do not replace the current counts above.

Empty extraction fields mean that information was not extracted. The data do not establish exhaustive coverage, independent human double screening, inter-rater agreement, regulatory compliance, or a pooled performance ranking.

Historical retrieval CSVs remain unchanged. [Legacy-data notes](docs/legacy-data.md) explain their limits. `python3 process-papers.py` reports possible duplicate matches without removing records. [Maintenance instructions](docs/maintenance.md) describe how to update the collection.

The [Apache 2.0 license](LICENSE) applies to this repository. Bibliographic metadata and links do not transfer rights to the cited publications. Third-party full texts and indexed abstracts are not redistributed.
