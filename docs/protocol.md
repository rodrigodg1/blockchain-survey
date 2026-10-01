# Scope and documented protocol

Version: 1 October 2026. This document describes the current manuscript and its available records; it does not reconstruct undocumented historical procedures.

## Review design and scope

The review is a structured qualitative survey of privacy, consent/permission management and decentralized or self-sovereign identity in blockchain-assisted data sharing. Governance is an analytical perspective on authority, enforcement, responsibility and evidence, not a new eligibility predicate or a claim to review all organizational or blockchain-protocol governance.

The research questions concern mechanisms for privacy and selective sharing; individual control of decentralized identity; platforms and their assumptions; and how identity, permission and confidentiality connect decision authority, enforcement and accountability. Comparison follows the protected information, the authorizing party, the enforcement component, remaining trust assumptions and the operation actually evaluated.

The application collection contains **136 studies and proposals: 46 privacy, 58 consent/permission and 32 identity records**. These groups follow the recorded extraction or retrieval-query family. They are accounting groups rather than mutually exclusive technical capabilities. Source provenance identifies 98 retained and 38 recent applications. The application collection is not uniformly recoded into a new governance taxonomy.

The public companion repository is [rodrigodg1/blockchain-survey](https://github.com/rodrigodg1/blockchain-survey). The canonical manuscript is `publications/survey-atualizar/main.tex` in the thesis repository.

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

On 1 October 2026, institutional access enabled Scopus S02/S05/S08, with 496/47/175 exported observations, and ACM S03/S06/S09, with 15/12/8 observations in the Full-Text Collection. The ACM date filter was January 2024 through September 2026. The Guide to Computing Literature was not searched. Scopus year-only matches require a primary publication-date check before admission. Expanded Scholar S01 pages 19--27 are retained (90 observations), while complete Scholar pagination remains unfinished.

The original [50 observations](../data/sources/revisao/protocol-search-records.csv) retain their native query/rank/date linkage and have the following current decisions:

| Disposition | Observed records |
|---|---:|
| Included after primary-text check | 38 |
| Awaiting sufficient primary full text | 1 |
| Completed application-scope exclusions | 3 |
| Review records | 6 |
| Review protocol | 1 |
| This manuscript | 1 |
| Total | 50 |

The 35-row follow-up assessment now records 30 inclusions, three application-scope exclusions, one review and one pending primary text. The original eight update inclusions are preserved. Seventeen of the 18 observations pending after the initial assessment are now resolved. Exact primary methods and boundaries for the latest 14 inclusions are in [search-completion-primary-evidence.md](../data/sources/revisao/search-completion-primary-evidence.md).

Additional exports contain 843 raw observations and 817 provisionally consolidated candidates. DOI matching applies only to nonempty normalized identifiers. Title-only matching remains provisional, and DOI-less observations are not silently merged with DOI-bearing records. Candidate retrieval and consolidation are separate from application eligibility. Their scientific screening is incomplete. The public metadata file omits indexed abstracts; the original raw-file hashes are retained in the snapshot. No complete historical search or screening total is reconstructed from these new counts.

## Eligibility and extraction

Recent inclusions must satisfy an original title predicate, concern a mechanism in the review's data-sharing scope, have a verifiable publication date/version, and provide accessible primary text supporting the extracted description. An identifiable workflow or mechanism and a source location are required. A study need not implement privacy, consent and identity simultaneously.

Assessment initially prioritized accessible primary texts and topics under revision. This affects the composition of a partial update and is documented as a selection limitation, not an additional eligibility criterion. Neither FHE nor QoE is a retrieval or inclusion requirement. The title interpretation distinguishes standalone `permission`/`permissions` from `permissionless` consensus terminology alone.

Empirical benchmarking and validation of every announced security property are not inclusion conditions. Descriptive eligibility and appraisal of claims are separate. Reviews are contextual related work rather than new application studies. Duplicate versions, out-of-window sources, sources outside title/scope requirements and candidates without sufficient primary evidence are not included in the recent comparison. Incomplete assessments are recorded as pending rather than completed exclusions.

[protocol-eligibility.csv](../data/sources/revisao/protocol-eligibility.csv) is an ancillary eligibility record: its 38 `include` entries agree with the recent extraction. Five prior exploratory title-predicate exclusions remain separate from the original 50 observed records and the additional retrieval. They are not added to either retrieval denominator.

The historical extraction records year, application, mechanism/contribution, platform and reported software availability. The recent extraction also records evaluation, evidence boundary, primary source URL and source location. Its 15-field source schema consists of the original 13 fields, the verified publication title and the additive `source_table` field linking each record to its specific comparison table. The normalized study CSV retains its existing schema. These describe the publications; the reviewed implementations were not independently rerun. A repository link does not establish maintenance, deployment or reproducible results.

Each exported study links to its original extraction record. Bibliographic title, author, year and DOI are resolved through the manuscript bibliography. Missing DOI is not a duplicate identifier. The exported collection has 136 distinct citation keys and normalized titles. Nonempty DOI uniqueness and missing-DOI counts are derived from the source records and reported in [counts.json](../data/counts.json), rather than imposed as fixed release-independent expectations.

## Context and synthesis

Related reviews, standards, legislation, regulatory guidance and official platform documentation support interpretation. They are not additional application studies and do not form a separately exhaustive legal or governance review. The manuscript's regulatory context was checked on 1 October 2026; the new retrieval is documented separately from these contextual checks.

The 67-record [synthesis matrix](../data/sources/revisao/synthesis-evidence-matrix.csv) and its [method note](../data/sources/revisao/synthesis-evidence-method.md) distinguish source version and access level, described mechanism, evaluated operation, boundary and requirement derivation. The bounded source selection supports G1–G8: identity/authority, authorization scope/state, key custody/release, confidentiality/correctness, audit/accountability, withdrawal/status, repeated-output inference and input provenance/truth. It is not uniform recoding of all 136 application records, a prevalence estimate or an evaluated reference architecture. Contextual standards and foundational research are not added applications.

The follow-up comparison identifies evidence genres and versions: Barnes is commentary proposing an original biobanking workflow without a functioning prototype; Oke is extracted from TechRxiv v1, with v2 explicitly unexamined; Al-Sabahi reports a formative questionnaire and extrapolated costs rather than measured registry deployment; Gupta verifies selected technical predicates on supplied inputs rather than determining legal compliance. These distinctions preserve descriptive eligibility while limiting the claims supported by each source.

The synthesis distinguishes a credential from authority, a permission record from its application, and an audit record from evidence of correct computation or lawful processing. Each computation check must identify its relation, inputs, claimed output, verifier and acceptance assumptions. The [alignment evidence](../data/sources/revisao/thesis-alignment-evidence.md) records selected implemented, proposed and potential connections. Multiple participants do not establish distributed trust or a universal need for computation proofs. Historical examples and recent comparisons identify design dependencies; they do not measure how prevalent complete integration is among all 136 records or in the wider literature.

## Limits

- Title-only retrieval, result ranking, access restrictions and incomplete assessment limit coverage, including coverage of 2024–2026.
- Complete historical screening counts, exclusions, reviewer assignments and agreement statistics are unavailable. The passage from raw exports to all 98 historical selections cannot be reproduced from those exports alone.
- Historical search totals differ between the former figure and available exports. The former deduplication incorrectly collapsed missing DOIs. Correcting the current script does not retroactively establish an improved historical selection.
- Evaluation fields were not extracted uniformly across historical and recent records. Empty historical fields mean unpopulated, not absence of limitations or evaluations.
- Extraction year and final bibliography year can differ because of publication-version metadata. A historical study with a later final issue year remains historical.
- The collection supports source-specific qualitative comparisons, not pooled performance rankings, completeness claims, compliance certification or endorsement of every security claim.

No PRISMA flow, independent human screening or inter-rater agreement is claimed. The current totals describe the documented collection and partial update.
