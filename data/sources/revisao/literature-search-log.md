# Supplementary literature update under the historical title protocol

Search/verification date: **2026-09-30** (America/Sao_Paulo). Publication window: **2024-01-01 through 2026-09-30**. This definitive log supersedes the broad exploratory selection preserved in `preliminary-discovery-log.md`. The controlling native retrieval records are `protocol-search-records.csv` and `protocol-retrieval-status.json`; they contain **50 observed result records and eight retained primary studies**. The historical collection remains **98 studies**, reported separately.

## Query predicates, interfaces, and actual retrieval

The original title scope is retained. The source-specific queries below reproduce the historical table; execution status does not imply that an inaccessible interface was searched.

| ID | Original interface / query | Execution on 2026-09-30 |
|---|---|---|
| S01 | Google Scholar: `allintitle: blockchain data privacy` | First result page; 10 observed records. |
| S02 | Scopus: `TITLE(blockchain) AND TITLE(data) AND TITLE(privacy)` | Not executed: document search required institutional authentication. |
| S03 | ACM DL: `[Title: blockchain] AND [Title: data] AND [Title: privacy]` | Not executed: advanced title search required Premium access. |
| S04 | Google Scholar: `allintitle: blockchain (consent OR permission)` | First three result pages; 30 observed records. |
| S05 | Scopus: `TITLE(blockchain) AND (TITLE(consent) OR TITLE(permission))` | Not executed: institutional authentication. |
| S06 | ACM DL: `[Title: blockchain] AND [[Title: consent] OR [Title: permission]]` | Not executed: Premium access. |
| S07 | Google Scholar: `allintitle: blockchain (decentralized OR self-sovereign) identity` | First result page; 10 observed records. |
| S08 | Scopus: `TITLE(blockchain) AND TITLE(decentralized OR self-sovereign) AND TITLE(identity)` | Not executed: institutional authentication. |
| S09 | ACM DL: `[Title: blockchain] AND [[Title: decentralized] OR [Title: self-sovereign]] AND [Title: identity]` | Not executed: Premium access. |

The coordinating agent executed these native Google Scholar searches with the publication-year filters `as_ylo=2024` and `as_yhi=2026`; publication/version dates were then checked against the 30 September cutoff. Native title/URL records were persisted by `save_protocol_records.py`, whose role is to save browser observations, not query a search API. Each CSV row gives the query, displayed title, URL, observed rank/page, date, filter, decision, and retained citation key. Exact within-day timestamps were not captured. The first pages are bounded observations, not a complete Scholar result export or the service's total matching-record count.

The exact S04 page-3 URL was:
`https://scholar.google.com/scholar?start=20&q=allintitle:+blockchain+(consent+OR+permission)&hl=pt-BR&as_sdt=0,5&as_ylo=2024&as_yhi=2026`.

An ACM exploratory `AllField=blockchain data privacy` query was not counted as S03/S06/S09. The update thus preserves the historical predicates and scope, but **does not complete a rerun of all three original databases or exhaustive pagination**. Scopus and ACM access limitations are explicit, rather than replaced with web-search domain filters.

## Eligibility and decisions

Primary inclusion requires (i) one of the historical title predicates; (ii) a relevant application, architecture, or mechanism for confidentiality, consent/permission, or decentralized identity in blockchain-assisted data sharing; (iii) a verified publication/version within the update interval; and (iv) accessible primary methods supporting the extraction. A study need not implement all three functions. Reviews, review protocols, duplicate versions, the authors' own manuscript, and title-ineligible credential constructions are not additional application studies. Related surveys, standards, and official project documentation have a separate contextual role.

The title predicates are blockchain + data + privacy; blockchain + (consent OR permission); or blockchain + (decentralized OR self-sovereign) + identity. Predicate checks use the actual verified publication title, with case and hyphenation normalized; a broad abstract-level association does not substitute for title eligibility. `protocol-eligibility.csv` records the selected titles and the correction of the original exploratory six-paper list.

The native CSV contains eight retained primary records, four awaiting primary full text, one copy of the manuscript, one review protocol, five review-related records, and 31 candidates whose full-text assessment remains incomplete. These statuses sum to the 50 observed records; they are **not a complete included/excluded PRISMA flow**. Unassessed candidates are not called exclusions. Assessment was opportunistic within these bounded observations: accessible full text and the topics under revision affected priority. No fixed prospective screening order or complete within-day sequence was recorded; ranking was not used as an eligibility or quality threshold. This is a selection limitation, not a reproducible ordering rule.

| Retained key | Native retrieval record | Verified title / matching predicate |
|---|---|---|
| `updateMasood2024Patient` | S01, rank 1, page 1 | A blockchain-based system for patient data privacy and security — blockchain/data/privacy. |
| `updateCan2024AuditableConsent` | S04, rank 4, page 1 | A Blockchain-Based Hybrid Architecture for Auditable Consent Management — blockchain/consent. |
| `updateJaved2024SecureConsent` | S04, rank 10, page 1 | SecureConsent: A Blockchain-Based Dynamic and Secure Consent Management for Genomic Data Sharing — blockchain/consent. |
| `updatePhuyal2026Architecture` | S04, rank 26, page 3 | A Blockchain-Based Architecture for Dynamic and Auditable Patient Consent in Secondary Use of Health Data — blockchain/consent. |
| `updateZeydan2024SSI` | S07, rank 3, page 1 | Blockchain-Based Self-Sovereign Identity: Taking Control of Identity in Federated Learning — blockchain/self-sovereign/identity. |
| `updateAgarkar2024BADIMAC` | S07, rank 1, page 1 | Blockchain aware decentralized identity management and access control system — blockchain/decentralized/identity. |

| `updateMaZhang2024Rollup` | S01, rank 5, page 1 | Integrating blockchain and ZK-ROLLUP for efficient healthcare data privacy protection system via IPFS — blockchain/data/privacy. |
| `updateDhasaratha2024IoMT` | S01, rank 6, page 1 | Data privacy model using blockchain reinforcement federated learning approach for scalable internet of medical things — blockchain/data/privacy. |

The historical extraction fields are retained: publication year, application, approach/contribution, platform, and reported implementation links. Evaluation settings and enforcement limits qualify the synthesis. A missing source link means not identified in the examined text, not that no implementation exists. Duplicate studies are checked through nonempty DOI and normalized title/version identity; a missing DOI is not treated as a duplicate identifier.

The initial exploratory table proposed Pham, Fang, BLS-MT-ZKP, CSD-JWT, Phuyal architecture, and COD-ssi. **Pham, Fang, BLS-MT-ZKP, CSD-JWT, and COD-ssi fail all historical predicates because blockchain is absent from their titles.** They were removed from the included update and its primary comparative analysis. The Phuyal architecture remains after its native S04 record and primary methods were verified. The previous web queries remain an honest exploratory record, without being retrospectively represented as native searches.

## Primary evidence and bibliography

The coordinating agent checked Masood and Zeydan through the platform-review subagent; their DOI metadata and method locations are recorded in `protocol-candidates-platforms.md` and `fontes-atualizacao/protocol-platforms/`. Masood's artifact supports a workflow comparison; inconsistencies in the performance analysis are not imported as quantitative gains. Zeydan's credential/authentication evaluation does not establish protection against model inference. These qualifications appear in the integrated eight-study table.

The remaining studies were checked as follows:

Published metadata were checked through Crossref REST `/works/<doi>` and the version-of-record or author article. Trimmed responses are retained in `fontes-atualizacao/`. Discovery snippets, vendor lists, and secondary reviews were not used instead of the primary methods.

| Included key | Verified publication / full text | Exact evidence location |
|---|---|---|
| `updateMasood2024Patient` | Multimedia Tools and Applications **83(21)**, **60443–60467** (2024); DOI [10.1007/s11042-023-17941-y](https://doi.org/10.1007/s11042-023-17941-y). [Published author-provided full text](https://www.researchgate.net/publication/377180997_A_blockchain-based_system_for_patient_data_privacy_and_security); publisher publication date verified as 5 January 2024. | 4.3–4.4; Table 6; 5. |
| `updateZeydan2024SSI` | IEEE Open Journal of the Communications Society **5**, **5764–5781** (2024); DOI [10.1109/OJCOMS.2024.3449692](https://doi.org/10.1109/OJCOMS.2024.3449692). [Published author-provided full text](https://www.researchgate.net/publication/383295952_Blockchain-based_Self-Sovereign_Identity_Taking_Control_of_Identity_in_Federated_Learning); bibliographic identity corroborated by Crossref and the CTTC record. | IV; V; VI.A and Table 2; VII.B. |
| `updateCan2024AuditableConsent` | IEEE Access **12**, 100419–100445 (2024); DOI [10.1109/ACCESS.2024.3431292](https://doi.org/10.1109/ACCESS.2024.3431292). Published article text read on [ResearchGate](https://www.researchgate.net/publication/382418870_A_Blockchain-Based_Hybrid_Architecture_for_Auditable_Consent_Management). The article header verifies publication **19 July 2024**, current version **29 July 2024**, DOI and pagination. IEEE's direct page presented robot verification; no bypass was attempted. | IV.B, V, VI, VII.A–D, IX. |
| `updateJaved2024SecureConsent` | 2024 International Conference on Smart Applications, Communications and Networking (SmartNets), **1–7**; DOI [10.1109/SmartNets61466.2024.10577693](https://doi.org/10.1109/SmartNets61466.2024.10577693). Full [author-provided paper](https://www.researchgate.net/publication/382033079_SecureConsent_A_Blockchain-Based_Dynamic_and_Secure_Consent_Management_for_Genomic_Data_Sharing), explicitly uploaded by Ibrahim Tariq Javed on 25 August 2024. Crossref verifies conference publication 28 May 2024. IEEE's direct page presented robot verification. | III.A–C, IV.A–B, V. |
| `updatePhuyal2026Architecture` | Blockchain in Healthcare Today **9(1)**, **28 April 2026**; DOI [10.30953/bhty.v9.491](https://doi.org/10.30953/bhty.v9.491). Full primary text from [PMC13378124](https://pmc.ncbi.nlm.nih.gov/articles/PMC13378124/), retrieved using the public NCBI BioC endpoint. | Study Design; Standards and Technology Selection; Scope of Revocation; Institutional Trust Assumptions. |
| `updateAgarkar2024BADIMAC` | Measurement: Sensors **31**, article **101032** (2024); available online **17 January 2024**; DOI [10.1016/j.measen.2024.101032](https://doi.org/10.1016/j.measen.2024.101032). Complete published [author-provided article](https://www.researchgate.net/publication/377479323_Blockchain_aware_decentralized_identity_management_and_access_control_system), uploaded by coauthor Lalit Kulkarni; published header and Crossref agree. | 3.1.1–3.1.3; 3.2.1–3.2.2; 4.1–4.2; 5–6; Figs. 5–8. |

| `updateMaZhang2024Rollup` | Scientific Reports **14(1)**, article **11746**, **23 May 2024**; DOI [10.1038/s41598-024-62292-9](https://doi.org/10.1038/s41598-024-62292-9). [Publisher full text](https://www.nature.com/articles/s41598-024-62292-9); the saved HTML/text and Crossref record are in `fontes-atualizacao/protocol-platforms/`. | Proposed model: Overview, Data flow and process, Figs. 2–4; Performance evaluation: Fig. 8 paragraph; Data availability. |
| `updateDhasaratha2024IoMT` | CAAI Transactions on Intelligence Technology, Early View, first published **6 February 2024**; DOI [10.1049/cit2.12287](https://doi.org/10.1049/cit2.12287). [Complete publisher HTML](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/cit2.12287) read again during the final audit; publisher and Crossref author/date metadata checked. No final issue/pagination inferred. | 3 Distributed Reinforcement Learning Approach; 5 Result Analysis; Tables 2–6; 6 Limitation. |

Crossref's Can entry provides only the year; the published article header resolves the day/month. Can's earlier SSRN preprint (10.2139/ssrn.4601868, 2023) is linked to the published study rather than counted separately. Qu's DOI contains 2024 while its volume 92 issue is March 2025; the article is within the interval either way, but publisher preview sections truncate its methods. No detailed comparative claims are derived from that preview.

The requested access retry yielded one further eligible descriptive proposal: BADIMAC, S07 rank 1. Its holder-approval and encrypted identity-sharing workflow supports extraction; the announced ZKP and retroactive erasure claims are not established by the described mechanisms. Inclusion does not certify those claims. The complete author-provided published text was inspected by the identity subagent and the coordinator.

No correction/retraction notice appeared in the available deposited update fields or accessible included-source headers. This is a limited status check, not a claim that notices cannot exist elsewhere.

## Related Work: four proximate surveys


The following are **secondary/contextual sources**, not newly included application studies:

| Key | Verified metadata and evidence read | Reason for comparison |
|---|---|---|
| `updateNguyen2025TrustworthySharing` | ACM Computing Surveys **57(8)**, article **195**, 36 pages; published **7 March 2025**; DOI [10.1145/3718082](https://doi.org/10.1145/3718082). The [ACM version of record](https://dl.acm.org/doi/10.1145/3718082) was accessed and read in full on the requested retry; header verifies the published nine-author record. Sections 4.3–4.4 and 6.3 support the architectural and privacy comparison. The earlier arXiv-only restriction is superseded. | Cross-domain sharing and BlockDaSh's processing, storage, and sharing subsystems; certificate-based identity verification, access/use policies and encrypted off-chain retrieval provide direct overlap with the workflow examined here. No comparative superiority or first joint coverage is inferred. |
| `updateLi2025HealthcareSharingReview` | Peer-to-Peer Networking and Applications **18(6)**, article **302**; **17 October 2025**; DOI [10.1007/s12083-025-02148-9](https://doi.org/10.1007/s12083-025-02148-9). [Publisher full text](https://link.springer.com/article/10.1007/s12083-025-02148-9), sections 3, 4.2.3–4.2.7 and 4.3. | Healthcare sharing stages, identity verification, access-control/consent patterns, privacy techniques, and maturity. Provides direct overlap rather than a distant generic blockchain survey. |
| `updatePhuyal2026ConsentReview` | JMIR Medical Informatics **14**, **e88536**, **22 June 2026**; DOI [10.2196/88536](https://doi.org/10.2196/88536). Full primary text from [PMC13287375](https://pmc.ncbi.nlm.nih.gov/articles/PMC13287375/). Methods, Consent Life Cycle Management, and Table 4 were checked. | Dynamic/withdrawable secondary-use consent, identity integration, off-chain propagation. Its 55/3/0 result is explicitly attributed, not imported as our result. Its authors also authored the conceptual architecture, so those papers are not independent confirmation. |
| `updateMazzocca2025DIDVC` | IEEE Communications Surveys & Tutorials **27(6)**, **3641–3671** (2025); DOI [10.1109/COMST.2025.3543197](https://doi.org/10.1109/COMST.2025.3543197). Full [author manuscript v2](https://arxiv.org/html/2402.02455v2), 16 April 2025, sections III.C, IV, V.B and VII; arXiv record identifies the published journal DOI. | DID/VC privacy, implementations, authorization applications, and adoption. Establishes existing privacy–identity overlap. |

The revised comparison describes positively verified focus and overlap. It does not infer topic absence from missing keywords, claim a first joint survey, or use broader domain coverage alone as evidence of a distinct contribution. Krul's SSI SoK and Ramić's selective-disclosure review remain verified exploratory records but were removed from the compact Related Work comparison to prioritize the four closer surveys above.

## Additional discovery and verification queries actually executed


These were `web.run` discovery/status/full-text searches; **none is a native database search**. No recency filter was used. Full dates were checked in the underlying records. The earlier exploratory query list is preserved separately.

| Exact query | Domain filter, if supplied |
|---|---|
| `"blockchain" "privacy" "consent" 2024 2025 2026 research` | none |
| `"blockchain" "self-sovereign identity" 2024 2025 paper` | none |
| `"blockchain" "data privacy" 2024 2025 survey consent` | none |
| `"Self-Sovereign Identity for Consented and Content-Based Access to Medical Records using Blockchain"` | none |
| `"blockchain" "data privacy" "2025" research -survey -review` | none |
| `"blockchain" "consent" "2024" paper -survey -review -reddit` | none |
| `blockchain consent 2025 architecture -review -survey` | link.springer.com; mdpi.com; dl.acm.org; sciencedirect.com; arxiv.org |
| `blockchain data privacy 2024 scheme -review -survey` | same publisher/repository filters as previous row |
| `"A blockchain- and self-sovereign identity-based collaborative framework"` | none |
| `"Self-Sovereign Identity for Consented" DOI conference` | none |
| `"A blockchain-based hybrid architecture for auditable consent management"` | none |
| `"A consent-aware electronic medical records sharing method based on blockchain"` | none |
| `"Secureconsent" "genomic data" 2024` | none |
| `"A Blockchain-Based Hybrid Architecture" "10.1109"` | none |
| `"SecureConsent" "Javed" "Lemieux"` | none |
| `"A blockchain-based hybrid architecture" pdf -researchgate -projectcentersinchennai` | none |
| `"Auditable Consent Management" pdf` | utdallas.edu; ege.edu.tr; arxiv.org; ieeexplore.ieee.org; utd.edu |
| `"SecureConsent" "pdf"` | ubc.ca; arxiv.org; ieeexplore.ieee.org |
| `"A consent-aware electronic" pdf` | arxiv.org; njupt.edu.cn; njnu.edu.cn; sciencedirect.com |
| `"3431292" pdf -researchgate -doaj -projectcentersinchennai` | none |
| `"SecureConsent" "10577693" pdf -researchgate -linkedin` | none |
| `"Auditable Consent Management" "Kantarcioglu" -researchgate -doaj` | none |
| `"SecureConsent" "2024" filetype:pdf -allmultidisciplinaryjournal -ge2p2global -proceedings -researchgate` | none |
| `"A Blockchain-Based Hybrid Architecture" filetype:pdf -researchgate -projectcentersinchennai` | none |
| `"Blockchain-Empowered Trustworthy Data Sharing" arxiv` | none |
| `"Blockchain-Empowered Trustworthy Data Sharing" pdf` | none |

Crossref REST title lookup `query.title=SecureConsent: A Blockchain-Based Dynamic and Secure Consent Management for Genomic Data Sharing&rows=3` returned the matching publication and two other records. Only the exact matching publication was verified for inclusion; that return count is not a screening denominator.

Encountered alternatives: Pava-Díaz et al. (10.3389/fbloc.2024.1443362) pass the identity title predicate but the publisher classifies the work as a review, so it is not a primary application. Tcholakian et al. (arXiv:2407.21559) pass the identity title predicate, but the reviewed publication and native retrieval record were not verified in this subtask. The smart-irrigation framework (10.1016/j.atech.2025.101654) passes the identity predicate, but native protocol retrieval was not verified; it was not added opportunistically. No unfavorable results or absence claims are inferred from these deferred candidates.

## Appraisal and limitations

Primary text was read against the described mechanism, artifact, evaluation setting, and stated limitations. No benchmark or security implementation was reproduced. Security properties are conditional on the reported assumptions. Query integrity, access-token validity, withdrawal propagation, and recall of disclosed data are distinct outcomes. A conceptual regulatory mapping is not deployment-level proof of compliance.

The partial native retrieval is subject to title terminology, result ranking, pagination, institutional access, and full-text availability limits. It does not estimate mechanism prevalence or establish that unassessed approaches are absent. Historical screening assignments, exclusion counts, PRISMA compliance, and human inter-rater agreement were not reconstructed or invented. The two Phuyal papers share authorship and are not independent confirmation. The related review's 55 underlying extractions were not audited individually.

`literature-update.tex` reports eight protocol-eligible primary studies; `related-work-revised.tex` contains the four proximate secondary comparisons. `related-work-update.tex` is a shorter alternative, not an additional section to input twice. Bibliographic records are preserved in `literature-update.bib`, `protocol-platforms-candidates.bib`, and `protocol-retry-included.bib`; unused exploratory entries are not rendered through citations. Technical and platform documents remain contextual sources, separately identified. The bounds of the retrieved set remain explicit in Methodology.

## Requested full-text access retry

The requested retry is documented in `retry-access-log.md`, with source-specific notes for Guan, Qu, and Seidi/Abdellaoui. Nguyen's ACM version of record was accessed and now supports a more specific Related Work comparison. The Wiley full text of S01 rank 6 was checked, but its examined methods did not support the intended privacy extraction; this is an evidence assessment, not an assertion that the title is ineligible. No abstract-only extraction was added.

## Final consistency reappraisal of extraction decisions

The previous decisions for S01 ranks 5 and 6 conflated insufficient evidence for claimed privacy/security with insufficient evidence for a descriptive extraction. The final audit corrected that inconsistency rather than introducing a quality threshold that the historical protocol did not document. Both sources have verifiable published primary texts, satisfy S01 and describe a relevant proposed workflow. They are now retained descriptively. This supersedes the earlier evidence-insufficient decisions; it does not validate their announced protection or numerical results.

The extraction requirement applied across all eight studies is an identifiable proposed workflow/mechanism, a supporting primary-text location, and explicit treatment of unspecified fields. Masood supports Composer ACL coordination; Ma/Zhang support a proposed RSA/IPFS/rollup workflow; Dhasaratha supports distributed learning/resource coordination; BADIMAC supports approval and encrypted identity sharing. Their integration, confidentiality, ZKP, or performance limitations remain appraisal findings. A benchmark, successful privacy proof, code repository, or implementation of all three functions is not an additional inclusion filter. Detailed decisions are in `reviewer-final-verification.md`.
