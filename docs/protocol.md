# Scope and documented protocol

Version: 1 October 2026. This document describes the current manuscript and its available records; it does not reconstruct undocumented historical procedures.

## Review design and scope

The review is a structured qualitative survey of privacy, consent/permission management and decentralized or self-sovereign identity in blockchain-assisted data sharing. Governance is an analytical perspective on authority, enforcement, responsibility and evidence, not a new eligibility predicate or a claim to review all organizational or blockchain-protocol governance.

The research questions concern mechanisms for privacy and selective sharing; individual control of decentralized identity; platforms and their assumptions; and how identity, permission and confidentiality connect decision authority, enforcement and accountability. Comparison follows the protected information, the authorizing party, the enforcement component, remaining trust assumptions and the operation actually evaluated.

The 98 historical studies are retained separately from 24 supplementary application records, totaling 122. The historical group sizes are 40/33/25; the current update adds 4/15/5, producing 44/48/30 combined. Follow-up assessment on 1 October 2026 retained 16 records from the initially pending set while preserving the original eight update inclusions. These are accounting groups. The historical tables are not uniformly recoded into a new governance taxonomy.

The public companion repository is [rodrigodg1/blockchain-survey](https://github.com/rodrigodg1/blockchain-survey). The canonical developing manuscript is `/Users/rodrigodgarcia/Desktop/phd-thesis/publications/survey-atualizar/main.tex`.

## Reported title queries

The historical search description uses Google Scholar, Scopus and ACM Digital Library, with no publication-year restriction. These are the reported predicates; listing a query does not establish that it was rerun for the update.

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

## Supplementary retrieval

On 30 September 2026, S01, S04 and S07 were rerun with a 2024–2026 publication-year filter and a cutoff of that date. The inspected pages were S01 page 1, S04 pages 1–3, and S07 page 1: respectively 10, 30 and 10 observed records. These are recorded observations, not estimates of all results returned or counts of unique publications across databases.

Scopus document search required institutional authentication. ACM advanced title search required Premium access. S02/S05/S08 and S03/S06/S09 were therefore not rerun. An exploratory ACM all-field query was not treated as an execution of a title query.

The 50 observations, including page/rank, date, displayed title, URL and disposition, are in [protocol-search-records.csv](../data/sources/revisao/protocol-search-records.csv). Their recorded dispositions are:

| Disposition | Observed records |
|---|---:|
| Included after primary-text check | 24 |
| Full-text/version assessment not completed | 1 |
| Awaiting sufficient primary full text | 17 |
| Completed application-scope/title-predicate exclusion | 1 |
| Review records, across the recorded review statuses | 5 |
| Review protocol | 1 |
| This manuscript, not a new study | 1 |
| Total | 50 |

The review, review-protocol and self-manuscript rows aggregate seven other dispositions for readability. The original status names are retained in [search-decision-counts.csv](../data/search-decision-counts.csv). Follow-up assessment on 1 October inspected all 35 initially pending observations: 16 were included, one was excluded, and 18 remain pending. The 50 original query/rank observations and the 30 September publication cutoff were preserved. [update-assessment-2026-10-01.csv](../data/sources/revisao/update-assessment-2026-10-01.csv) records prior/current decisions, genre, version, access status, evidence locations and reasons. This assessment is not a new search round, and its 18 pending records are not excluded studies.

## Eligibility and extraction

Recent inclusions must satisfy an original title predicate, concern a mechanism in the review's data-sharing scope, have a verifiable publication date/version, and provide accessible primary text supporting the extracted description. An identifiable workflow or mechanism and a source location are required. A study need not implement privacy, consent and identity simultaneously.

Assessment initially prioritized accessible primary texts and topics under revision. This affects the composition of a partial update and is documented as a selection limitation, not an additional eligibility criterion. Neither FHE nor QoE is a retrieval or inclusion requirement. The title interpretation distinguishes standalone `permission`/`permissions` from `permissionless` consensus terminology alone.

Empirical benchmarking and validation of every announced security property are not inclusion conditions. Descriptive eligibility and appraisal of claims are separate. Reviews are contextual related work rather than new application studies. Duplicate versions, out-of-window sources, sources outside title/scope requirements and candidates without sufficient primary evidence are not included in the recent comparison. Incomplete assessments are recorded as pending rather than completed exclusions.

[protocol-eligibility.csv](../data/sources/revisao/protocol-eligibility.csv) is a 29-row ancillary eligibility log: 24 `include` entries agree with the recent extraction and five prior exploratory candidates fail the blockchain title predicate. It is not the master decision log for all 50 observations or all 122 included records. Its five exploratory exclusions are separate from the single newly completed exclusion and five review records among the 50 observed query results; they must not be added to that retrieval denominator or to the application collection.

The historical extraction records year, application, mechanism/contribution, platform and reported software availability. The recent extraction also records evaluation, evidence boundary, primary source URL and source location. Its 15-field source schema consists of the original 13 fields, the verified publication title and the additive `source_table` field linking each record to its specific comparison table. The normalized study CSV retains its existing schema. These describe the publications; the reviewed implementations were not independently rerun. A repository link does not establish maintenance, deployment or reproducible results.

Each exported study links to its original extraction record. Bibliographic title, author, year and DOI are resolved through the manuscript bibliography. Missing DOI is not a duplicate identifier. The exported collection has 122 distinct citation keys and normalized titles. Nonempty DOI uniqueness and missing-DOI counts are derived from the source records and reported in [counts.json](../data/counts.json), rather than imposed as fixed release-independent expectations.

## Context and synthesis

Related reviews, standards, legislation, regulatory guidance and official platform documentation support interpretation. They are not additional application studies and do not form a separately exhaustive legal or governance review. The manuscript's regulatory context was checked on 1 October 2026; this repository synchronization performed no new source retrieval.

The 53-record [synthesis matrix](../data/sources/revisao/synthesis-evidence-matrix.csv) and its [method note](../data/sources/revisao/synthesis-evidence-method.md) distinguish source version and access level, described mechanism, evaluated operation, boundary and requirement derivation. The bounded source selection supports G1–G8: identity/authority, authorization scope/state, key custody/release, confidentiality/correctness, audit completeness/disclosure, withdrawal/status, repeated-output inference and input provenance/truth. It is not uniform recoding of all 122 application records, a prevalence estimate or an evaluated reference architecture. Contextual standards and foundational research are not added applications.

The follow-up comparison identifies evidence genres and versions: Barnes is commentary proposing an original biobanking workflow without a functioning prototype; Oke is extracted from TechRxiv v1, with v2 explicitly unexamined; Al-Sabahi reports a formative questionnaire and extrapolated costs rather than measured registry deployment; Gupta verifies selected technical predicates on supplied inputs rather than determining legal compliance. These distinctions preserve descriptive eligibility while limiting the claims supported by each source.

The synthesis distinguishes a credential from authority, a permission record from its application, and an audit record from evidence of correct computation or lawful processing. Historical examples and recent comparisons identify design dependencies; they do not measure how prevalent complete integration is among all 122 records or in the wider literature.

## Limits

- Title-only retrieval, result ranking, access restrictions and incomplete assessment limit coverage, including coverage of 2024–2026.
- Complete historical screening counts, exclusions, reviewer assignments and agreement statistics are unavailable. The passage from raw exports to all 98 historical selections cannot be reproduced from those exports alone.
- Historical search totals differ between the former figure and available exports. The former deduplication incorrectly collapsed missing DOIs. Correcting the current script does not retroactively establish an improved historical selection.
- Evaluation fields were not extracted uniformly across historical and recent records. Empty historical fields mean unpopulated, not absence of limitations or evaluations.
- Extraction year and final bibliography year can differ because of publication-version metadata. A historical study with a later final issue year remains historical.
- The collection supports source-specific qualitative comparisons, not pooled performance rankings, completeness claims, compliance certification or endorsement of every security claim.

No PRISMA flow, independent human screening or inter-rater agreement is claimed. The current totals describe the documented collection and partial update.
