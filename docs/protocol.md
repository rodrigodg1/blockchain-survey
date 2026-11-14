# Survey protocol and evidence scope

The publication cutoff is 30 September 2026.

## Review design and accounting

The qualitative survey covers privacy, consent/permission management and decentralized identity. Its 139 included publications comprise 48 privacy, 59 consent and 32 identity records. Each publication is counted in one search-topic group, and all contribute to the classification of applications and mechanisms. The qualitative synthesis examines selected data-sharing operations involving multiple stakeholders. One publication may describe several operations.

RQ1 concerns privacy, consent and selective sharing. RQ2 concerns individual identity control. RQ3 concerns enabling platforms and protocols. The exact questions are recorded in [collection-membership.json](../data/sources/revisao/collection-membership.json), together with the six inventory memberships, evaluation extraction identities, and evaluation presentation locations.

## Title queries

The collection spans publications available by the cutoff with no lower publication-year limit. Some retained [search records](../data/sources/revisao/protocol-search-records.csv) document a 2024–2026 filter for the corresponding retrievals; that filter is not a lower publication-year limit for the complete collection.

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

The comparisons examine the participating entities, the services enforcing permissions, data and decryption-key custody, and the information disclosed to recipients. Reported evaluations are interpreted according to the operations and trust assumptions they address. Differences in study scope and reporting limit which dimensions can be compared. Each comparison identifies its supporting publications, and details are extracted only where supported by the sources.

The [evidence matrix](../data/sources/revisao/synthesis-evidence-matrix.csv) links comparisons of sharing operations, enforcement points, trust assumptions, and reported evaluations to their sources. The [codebook](../data/sources/revisao/synthesis-codebook.md) defines the extraction fields. The [derivation register](../data/sources/revisao/requirement-derivation.csv) links individual observations to the evaluation objectives.

The synthesis distinguishes findings reported by the original studies from the authors' comparative interpretation. The qualitative comparisons inform the eight evaluation objectives, G1–G8; they do not establish new security guarantees. Evaluation records and presentation locations identify retained evidence, not uniform analytical coverage of all 139 publications.

The platform comparison uses the documented versions and access dates of its sources, as recorded in the retained bibliography. It is qualitative, does not independently verify security claims, and does not rank platforms.

The timeline counts explicit names in existing descriptions, using all 139 publications in its denominators. It does not measure adoption or effectiveness. The earlier two-study processing-cost illustration is excluded from the current figure set because it describes only two studies. Its retained inputs and original generator support optional historical reproduction. [Plot method](../data/sources/revisao/technology-timeline-method.md), [measurement records](../data/sources/revisao/processing-costs-data.json), [reproduction instructions](../REPRODUCE.md).

## Inference limits

The literature search was selective. Title-based retrieval, ranking, and source access constrain coverage. The survey supports qualitative comparisons and descriptive counts for the included publications. System performance and security findings apply within the assumptions and evaluation conditions documented for each source.
