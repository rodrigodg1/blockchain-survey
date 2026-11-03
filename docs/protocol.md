# Survey protocol and evidence scope

Snapshot: 4 November 2026. The publication cutoff remains 30 September 2026. This document describes recorded procedures and preserves unresolved historical and retrieval limitations.

## Review design and accounting

The qualitative survey covers privacy, consent/permission management and decentralized identity. Its 139 included publications comprise 48 privacy, 59 consent and 32 identity records. Search-topic groups support counting and do not imply disjoint capabilities. The analytical unit is a sharing or processing operation; one publication may describe several operations.

RQ1 concerns privacy, consent and selective sharing. RQ2 concerns individual identity control. RQ3 concerns enabling platforms and protocols. The exact manuscript questions are recorded in [manuscript-membership.json](../data/sources/revisao/manuscript-membership.json), together with the six inventory-table memberships and repeated evaluation entries.

The historical collection contains 98 records (40/33/25). The 41 additions contain 8 privacy, 26 consent and 7 identity publications. Search decisions, not retrieval counts or bibliography size, establish inclusion.

## Title queries

The historical description has no lower publication-year limit. The contemporary searches applied 2024–2026 filters and the publication cutoff above. Listing a predicate does not establish complete retrieval or screening.

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

## Recorded retrieval and decisions

On 30 September 2026, the original Scholar observations covered S01 page 1, S04 pages 1–3 and S07 page 1: 10, 30 and 10 records. Their current decisions remain separate from later retrieval:

| Original Scholar disposition | Records |
|---|---:|
| Included | 38 |
| Pending sufficient primary text | 1 |
| Excluded for application scope | 3 |
| Reviews | 6 |
| Review protocol | 1 |
| This manuscript | 1 |
| **Total** | **50** |

On 1 October 2026, Scopus S02/S05/S08 exports contained 496/47/175 observations. ACM S03/S06/S09 contained 15/12/8 observations in the Full-Text Collection, filtered to January 2024 through September 2026. ACM's Guide to Computing Literature was not searched. Scopus year-only matches required primary publication-date checking. Retained expanded Scholar S01 pages 19–27 contain 90 observations; complete Scholar pagination remains unfinished.

These additional exports contain 843 observations and 817 provisionally consolidated candidates. Their current dispositions are 777 awaiting title/abstract screening, 36 matches to existing included publications, two pending primary text and two retained after assessment. The two retained Scopus S02 publications are InvisiReveal and the distributed-KMS study, assessed on 26 October 2026. [Assessment records](../data/sources/revisao/database-update-extraction-2026-10-26.csv).

A separate targeted S04 follow-up on 26 October assessed one author-suggested sports-data paper at observed rank 54 (page 6). It met the same cutoff and eligibility conditions. Intervening results were not systematically screened. This inclusion is outside both the original 50 observations and the 817 additional candidates. [Native follow-up record](../data/sources/revisao/protocol-followup-records-2026-10-26.csv).

The included total is therefore **98 + 38 + 2 + 1 = 139**. `run.py` verifies the three addition strata independently. The ancillary `protocol-eligibility.csv` documents the original 38 inclusions and separate exploratory exclusions; it is not the master log for every retrieval stratum. Indexed abstracts are omitted from public candidate metadata; raw-export fingerprints remain in the source snapshot.

## Eligibility, identities and extraction

Available recent screening records require a matching title family, a blockchain-assisted application or control involving user-data protection, consent/permission or decentralized identity, an accessible primary description and a verifiable date/version. A paper need not implement all three functions. Conceptual designs, commentary containing an original workflow, preprints and evaluated systems are eligible. Reviews are contextual related work. Incomplete assessments remain pending.

Assessment prioritized accessible primary descriptions and topics under comparison. Neither FHE nor QoE is an inclusion requirement. Standalone permission/permissions is distinguished from permissionless consensus terminology. Selection was not exhaustive, and historical selection decisions cannot be reconstructed completely.

DOI matching uses nonempty normalized identifiers. Missing DOI is not a duplicate identifier. Title matches remain provisional where metadata or versions conflict. The current included dataset has 139 unique citation keys and normalized titles, including 130 distinct nonempty DOIs. Every exported row links to its extraction record, native retrieval reference where available, bibliography and inventory table. Date bases remain separate: extraction year and final bibliography year can differ without creating a new inclusion.

The source bibliography classifies 137 works as journal articles, conference contributions or book chapters, plus two preprints: ClinConNet arXiv v1 and the FHIR oncology consent proposal TechRxiv v1. Peer review was not individually verified for all 137 published records. Source access is distinct from independent reproduction or endorsement of a security claim.

## Detailed synthesis and figures

The [70-row matrix](../data/sources/revisao/synthesis-evidence-matrix.csv) contains 53 application publications and 17 contextual sources. The 53 comprise all 41 additions and 12 historical examples, chosen retrospectively to compare contrasting operations and control points. They are not a representative sample. The other 86 publications were not uniformly coded against G1–G8.

Application access records distinguish 37 direct full-text checks, nine source-specific assessment-stage full-text checks and seven limited or unverified sources. The latter do not support new algorithm-level or performance claims. The [codebook](../data/sources/revisao/synthesis-codebook.md) and [derivation register](../data/sources/revisao/requirement-derivation.csv) preserve the path from source observations and their limits to conditional evaluation objectives. Stored associations do not independently validate interpretation or establish requirement satisfaction.

Separate evaluation tables repeat 8 privacy, 26 consent and 7 identity publications. These 41 summaries add no publications to the inventory. Omission means no evaluation/limit detail was extracted for that table, not that the study has no evaluation.

The timeline counts explicit names in existing descriptions, using all 139 publications in its denominators. It does not measure adoption or effectiveness. Processing-cost plots reuse two included papers' reported measurements without pooling performance across systems. [Plot method](../data/sources/revisao/technology-timeline-method.md), [measurement records](../data/sources/revisao/processing-costs-data.json), [reproduction instructions](../REPRODUCE.md).

## Inference limits

Title-only retrieval, ranking, access restrictions and incomplete screening limit coverage. Historical reviewer assignments, complete exclusions and agreement statistics are unavailable. The historical DOI-empty deduplication error does not become a valid selection rule through preservation; correcting current processing does not reconstruct the historical selection.

The synthesis is retrospective and had automated research/extraction assistance. No independent human double coding, inter-rater reliability, literature saturation assessment, new primary experiment, exhaustive search or compliance certification is claimed. Missing evidence is not an observed attack. The dataset supports bounded qualitative comparisons and descriptive counts, not prevalence estimates or system-performance rankings.
