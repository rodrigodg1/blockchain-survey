# Publication timeline: scope and reproducibility

## Purpose and limits

The timeline describes named approaches in the existing 139-publication inventory. It uses 12 figure annotations: seven processing-related approaches and five identity models, features, or implementations. These annotations are not new mutually exclusive study classes, RQs, or eligibility criteria. The original 48 privacy, 59 consent, and 32 identity memberships remain unchanged. Named general encryption and unspecified identity services are not silently assigned to a particular cryptosystem or implementation.

The unit counted is one publication per feature and bibliography year. A publication may contribute to several series. Panels (a) and (b) show the seven processing-related approaches, split into encryption and proofs/learning. Panel (c) shows the five identity annotations. The manuscript discusses combinations through cited examples of their functions rather than a separate panel of sparse publication dates. The auxiliary combinations CSV retains the seven publications that have both processing and identity annotations, grouped into four exact profiles among the twelve features. Each publication appears in exactly one profile; no pairwise expansion or counting of all feature subsets is performed. Other technologies outside the twelve annotations are not represented by these profiles. A zero-knowledge credential can generate both the ZK and CREDENTIAL annotations, so the profiles do not imply independent controls or validated integration.

The figure uses four fixed, non-overlapping publication windows: 2015--2017, 2018--2020, 2021--2023, and 2024--2026. Their denominators are 5, 29, 62, and 43, respectively. The last window ends at the survey's 30 September 2026 publication cutoff. Each percentage pools the number of distinct publications naming the feature and divides by **all** included publications in that window. It is not an unweighted average of annual percentages. Papers with no plotted feature remain in the denominator. The annual counts and source keys remain available in `technology-timeline-counts.csv`.

Three-year pooling reduces dependence on small annual counts, but loses within-window timing. No smoothing, regression, significance test, or confidence interval is applied. Lines in panels (a)--(c) connect descriptive proportions only. Panel (c) uses a wider vertical range than the other panels, with percentage ticks shown on every axis. Period normalization does not correct selective retrieval or uneven extraction. In particular, the consent group grows from 17/62 publications in 2021--2023 to 26/43 in 2024--2026, so changes in group composition can affect the plotted proportions. The period CSV records all three group denominators to make that limitation inspectable.

The plot describes 61 publications with at least one selected explicit name. The other 78 remain part of the inventory and denominators. Zero means no recorded mention in these fields; it does not establish absence of a technology. Counts and proportions are not evidence of implementation, effectiveness, maturity, technology invention, adoption, replacement of one technology by another, or a statistically estimated trend. Differential privacy includes a reported proposal whose calibration is not established, and federated learning does not itself establish confidentiality. Credentials of different formats share a descriptive series without being treated as interchangeable.

## Data and date rules

The generator reads only:

- The six application-inventory tables in `main.tex`: application and control/method cells.
- `historical-extraction.csv`: reported technique and contribution.
- `recent-extraction.csv`: application and approach.
- `synthesis-evidence-matrix.csv`: operation and reported mechanism, where a source is present.
- `references-revised.bib`: the publication year used by the manuscript's citations.

Evaluation/limits and background sections are excluded from term matching to avoid counting a negated property or an unrelated background technology. An explicit vocabulary maps names and abbreviations to plot rows. Every match retains its source field and complete existing description for inspection. Uppercase PRE and FL are case-sensitive so that, for example, "pre-access" is not interpreted as proxy re-encryption. Proposals are retained as descriptions, not promoted to evaluated systems. Access status is copied from the existing matrix, or marked inventory-only.

Using the bibliography resolves three differences from stored extraction-year labels: MedShare is plotted in 2023, and DOI records 10.1109/jiot.2023.3307073 and 10.1109/jiot.2023.3296460 in 2024. The citation key 10.1109/jiot.2021.3134755 is plotted in 2023, as in the bibliography and table, not in the year embedded in its DOI. No underlying year or bibliographic record is changed.

Feature rows are intentionally restricted to explicit descriptions. RISC0 and generic rollup validity proofs are not automatically relabeled as zero-knowledge proofs from an implementation name alone. Manual re-encryption by a patient is not counted as proxy re-encryption. Attribute-based credentials are not counted as attribute-based encryption. Future editing of source descriptions can change recorded mentions without representing a change in the scientific literature.

## Critical reading of co-reporting

Seven publications have both processing and identity annotations:

| Publication key | Bibliography year | Relationship recorded | Existing access status |
|---|---:|---|---|
| 2021-did-prevent-secondary | 2021 | Homomorphic computation with identity and credentials | Direct full text |
| 2022-towards-ssi-privacy-fl | 2022 | SSI, federated learning and differential privacy described | Primary preview only |
| 10.1109/tc.2023.3251846 | 2023 | Attribute-based credentials and zero-knowledge proofs | Inventory only |
| updateHu2024InvisiReveal | 2024 | ZK credentials and authorization | Indexed primary sections |
| updateZeydan2024SSI | 2024 | SSI credentials for federated-learning authentication | Direct full text |
| updateHussain2025ZeroTrust | 2025 | Proposed local differential privacy/federated learning with SSI | Direct full text; privacy calibration remains unresolved |
| updateAlSabahi2026AuthorshipConsent | 2026 | Consent credentials and proposed affiliation-set proof | Direct full text; conceptual design |

This is evidence of co-description, not seven independently validated privacy/identity integrations. The manuscript uses the available evaluation boundaries to contrast encrypted computation, participant authentication, and permission checks. The limited-source examples supply descriptive chronology only.

## Reproduce and audit

```sh
python3 revisao/plot_technology_timeline.py
```

Requires Matplotlib and NumPy. Outputs:

- `imgs/technology-timeline.pdf`: vector figure. An optional `--preview /tmp/technology-timeline.png` argument writes a raster preview without adding an unused image to `imgs/`.
- `technology-timeline-records.csv`: all 139 original identities, publication years, original groups, source-access status, and figure annotations.
- `technology-timeline-matches.csv`: source fields, matched names and existing descriptions behind every annotation.
- `technology-timeline-counts.csv`: each cell's count, annual denominator, and full list of publication keys.
- `technology-timeline-periods.csv`: pooled counts, denominators, percentages, original-group composition, and publication keys for every plotted point.
- `technology-timeline-combinations.csv`: auxiliary record of exact feature profiles, readable labels, period membership, publication years, and source keys. These profiles are retained for audit and are not plotted.

Assertions check unique identities, membership equality, the original 48/59/32 group counts, and known year/abbreviation traps. Counts can be independently recomputed from the records CSV, and each annotation can be checked against its retained source description. No primary study, platform-only reference, or theoretical background paper is added to the inventory. The figure adds no independent primary-text verification or uniform quality assessment.
