# Survey protocol and evidence scope

The publication cutoff is 30 September 2026.

## Review design and accounting

The qualitative survey covers privacy, consent/permission management and decentralized identity. Its 139 included publications comprise 48 privacy, 59 consent and 32 identity records. Each publication is counted in one search-topic group. The analytical unit is a sharing or processing operation, and one publication may describe several operations.

RQ1 concerns privacy, consent and selective sharing. RQ2 concerns individual identity control. RQ3 concerns enabling platforms and protocols. The exact questions are recorded in [collection-membership.json](../data/sources/revisao/collection-membership.json), together with the six inventory memberships, evaluation extraction identities, and evaluation presentation locations.

## Title queries

The collection spans publications available by the cutoff with no lower publication-year limit. Where applied, database filters covered 2024–2026.

| ID | Source | Reported query |
|---|---|---|
| S01 | Google Scholar | `allintitle: blockchain data privacy` |
| S02 | Scopus | `TITLE(blockchain) AND TITLE(data) AND TITLE(privacy)` |
| S03 | ACM DL | `[Title: blockchain] AND [Title: data] AND [Title: privacy]` |
| S04 | Google Scholar | `allintitle: blockchain (consent OR permission)` |
| S05 | Scopus | `TITLE(blockchain) AND (TITLE(consent) OR TITLE(permission))` |
| S06 | ACM DL | `[Title: blockchain] AND [[Title: consent] OR [Title: permission]]` |
| S07 | Google Scholar | `allintitle: blockchain (decentralized OR self-sovereign) identity` |
| S08 | Scopus | `TITLE(blockchain) AND TITLE(decentralized OR self-sovereign) AND TITLE(identity)` |
| S09 | ACM DL | `[Title: blockchain] AND [[Title: decentralized] OR [Title: self-sovereign]] AND [Title: identity]` |

## Eligibility, identities and extraction

The recorded eligibility criteria include a matching title family, a blockchain-assisted application or control involving user-data protection, consent/permission or decentralized identity, an accessible primary description and a verifiable date/version. A study need not implement all three functions. Conceptual designs, commentary containing an original workflow, preprints and evaluated systems are eligible. Reviews are contextual related work.

Assessment prioritized accessible primary descriptions and topics under comparison. The consent query uses permission in the sense of authorization to access or use data.

DOI matching uses nonempty normalized identifiers. Missing DOI is not a duplicate identifier. Title matches remain provisional where metadata or versions conflict. The current included dataset has 139 unique citation keys and normalized titles, including 130 distinct nonempty DOIs. Every exported row links to its extraction record, native retrieval reference where available, bibliography and inventory table. Date bases remain separate: extraction year and final bibliography year can differ without creating a new inclusion.

The source bibliography classifies 137 works as journal articles, conference contributions or book chapters, plus two preprints: ClinConNet arXiv v1 and the FHIR oncology consent proposal TechRxiv v1. Peer review was not individually verified for all 137 published records. Source access is distinct from independent reproduction or endorsement of a security claim.

## Synthesis and figures

The [evidence matrix](../data/sources/revisao/synthesis-evidence-matrix.csv) links comparisons of sharing operations, enforcement points, trust assumptions, and reported evaluations to their sources. The [codebook](../data/sources/revisao/synthesis-codebook.md) defines the extraction fields. The [derivation register](../data/sources/revisao/requirement-derivation.csv) links individual observations to the evaluation objectives.

The evaluation records describe the operations tested and the conditions reported by the included publications. The synthesis excerpts identify the evaluations discussed in each section.

The timeline counts explicit names in existing descriptions, using all 139 publications in its denominators. It does not measure adoption or effectiveness. The earlier two-study processing-cost illustration is excluded from the current figure set because it describes only two studies. Its retained inputs and original generator support optional historical reproduction. [Plot method](../data/sources/revisao/technology-timeline-method.md), [measurement records](../data/sources/revisao/processing-costs-data.json), [reproduction instructions](../REPRODUCE.md).

## Inference limits

The literature search was selective. Title-based retrieval, ranking, and source access constrain coverage. The survey supports qualitative comparisons and descriptive counts for the included publications. System performance and security findings apply within the assumptions and evaluation conditions documented for each source.
