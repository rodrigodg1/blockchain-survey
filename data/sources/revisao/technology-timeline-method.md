# Publication timeline: data and interpretation

The chronology counts explicit approach names in a fixed inventory of 139 publications: 48 privacy, 59 consent, and 32 identity records. The twelve annotations do not replace those groups and are not mutually exclusive technical classes.

## What each point represents

The publication windows are 2015–2017, 2018–2020, 2021–2023, and 2024–2026. Their denominators are 5, 29, 62, and 43. The publication cutoff and retrieval limits are recorded in the [protocol](../../../docs/protocol.md).

For each approach and window, the numerator is the number of distinct publications with a recorded mention. The percentage is that count divided by all included publications in the window, multiplied by 100. Publications with no selected annotation remain in the denominator. The calculation does not average annual percentages.

A total of **62 publications** name at least one selected approach; 77 name none in the retained fields. Zero means no recorded mention, not demonstrated absence of a technology. A publication can contribute to multiple series.

The proxy re-encryption annotation for `2021-data-priv-iot` contributes to the 2021–2023 numerator. That point is **4/62 = 6.45%**. This description update changes a recorded annotation without adding a publication or changing its group or bibliography year.

## Inputs and matching

The generator uses:

- Application and approach cells in [application-inventory.tex](application-inventory.tex).
- Reported techniques and contributions in [historical-extraction.csv](../historical-extraction.csv).
- Application and approach fields in [recent-extraction.csv](recent-extraction.csv).
- Operations and mechanisms in [synthesis-evidence-matrix.csv](synthesis-evidence-matrix.csv).
- Publication years in [references-revised.bib](../references-revised.bib).

Evaluation limitations and background prose are excluded from term matching. Each match retains its source field, matched term, and original description in [technology-timeline-matches.csv](technology-timeline-matches.csv).

The twelve series are homomorphic encryption, attribute-based encryption, proxy re-encryption, searchable encryption, zero-knowledge proofs or credentials, federated learning, differential privacy, DID/SSI, credentials, Indy/Aries, Veramo, and IOTA Identity. These series mix mechanisms, identity models, credential features, and implementations. Their presence does not establish equivalent privacy guarantees.

Uppercase PRE and FL are case-sensitive. The expression “pre-access” is not interpreted as proxy re-encryption. Attribute-based credentials are not treated as attribute-based encryption. Patient-managed re-encryption is not automatically counted as proxy re-encryption. RISC0 and generic rollup validity proofs are not automatically classified as zero-knowledge proofs. Proposals remain descriptions of proposed behavior.

Bibliography years determine the windows. MedShare is counted in 2023. The DOI records `10.1109/jiot.2023.3307073` and `10.1109/jiot.2023.3296460` are counted in 2024. The year embedded in a citation key is not used as a substitute for a publication year.

## Interpretation limits

Three-year pooling hides variation within each window. Connecting lines describe proportions; they do not represent fitted trends. No smoothing, regression, significance test, or confidence interval is applied. The identity panel uses a wider vertical scale, with percentage ticks shown on every axis.

Period normalization does not correct selective retrieval or uneven extraction. Consent publications account for 17/62 records in 2021–2023 and 26/43 in 2024–2026, so changes in group composition can affect the proportions. The period data retain all three group denominators.

Recorded mentions do not establish adoption, implementation, effectiveness, maturity, technology replacement, or independent validation. Federated learning alone does not establish confidentiality. The differential-privacy series includes a proposal without sufficient calibration details. Different credential formats remain distinguishable in the source descriptions even when grouped in one plotted series.

Seven publications contain both processing and identity annotations: `2021-did-prevent-secondary`, `2022-towards-ssi-privacy-fl`, `10.1109/tc.2023.3251846`, `updateHu2024InvisiReveal`, `updateZeydan2024SSI`, `updateHussain2025ZeroTrust`, and `updateAlSabahi2026AuthorshipConsent`. The combinations file groups them into four exact profiles. A zero-knowledge credential may produce both ZK and CREDENTIAL annotations. Co-description does not establish independent controls or validated integration.

## Reproduction and trace files

From the repository root, after installing the plotting dependencies:

```sh
.venv/bin/python reproduce_plots.py
.venv/bin/python reproduce_plots.py --validate
```

The commands and environment are documented in [REPRODUCE.md](../../../REPRODUCE.md). Outputs are `data/figures/technology-timeline.pdf`, its PNG preview, and the figure manifest. Five retained trace files must agree with regeneration:

| File | Contents |
|---|---|
| [technology-timeline-records.csv](technology-timeline-records.csv) | 139 identities, bibliography years, groups, access labels, and annotations |
| [technology-timeline-matches.csv](technology-timeline-matches.csv) | Source descriptions behind every annotation |
| [technology-timeline-counts.csv](technology-timeline-counts.csv) | Annual feature counts, denominators, and publication keys |
| [technology-timeline-periods.csv](technology-timeline-periods.csv) | Every plotted count, denominator, percentage, group composition, and publication key |
| [technology-timeline-combinations.csv](technology-timeline-combinations.csv) | Exact combined profiles for the seven co-described publications |

All 139 identities are preserved. Contextual and platform references do not enter the publication denominators. The trace files allow independent recomputation of every point; they do not substitute for primary-source interpretation or a uniform quality assessment.
