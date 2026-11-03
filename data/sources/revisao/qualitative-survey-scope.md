# Adopted scope: structured qualitative survey

The authors chose on 2026-10-01 to preserve the structured qualitative survey, documenting criteria, searches, extraction, synthesis, and limitations. This record explains the current procedure; it is not a prospectively registered protocol or a reconstruction of historical screening.

On 2 October 2026, the author explicitly reaffirmed that this is not a systematic review. Adequacy is assessed against the bounded comparison questions: identifiable source selection, traceable observations, restricting conditions, and conclusions consistent with the selected evidence. Exhaustive candidate screening, PRISMA reporting, and independent human double coding are not automatic acceptance conditions for this objective. Their absence still limits coverage or extraction-confidence claims.

The current title is **Blockchain-Assisted Data Sharing: A Survey of Privacy, Consent, and Self-Sovereign Identity**. On 26 October 2026, the author requested restoration of the original RQs and clarified that eligibility concerns use of user data. Governance and verification remain complementary analytical dimensions. It does not introduce a new application eligibility predicate or a comprehensive review of organizational governance or blockchain protocol governance.

## Objective and justification

The survey compares how confidentiality, consent or permission, and identity connect in blockchain-assisted sharing. The collection includes conceptual workflows and evaluated implementations with different operations, workloads, and evidence. A qualitative comparison can examine their dependencies without pooling incompatible measurements, estimating prevalence, or assigning a common effectiveness score. Preserving historical identities and search predicates establishes continuity, not complete coverage or validity of every source claim.

## Current procedure and evidence strata

| Element | Delimitation |
|---|---|
| Application scope | Confidentiality, consent/permission, or decentralized/SSI identity in a blockchain-assisted workflow using user data. Not every study must implement all three. |
| Historical collection | 98 retained identities; inherited platform/software fields were not uniformly revalidated. |
| Supplementary retrieval | Original title predicates; 2024–2026 filter and cited-version cutoff of 2026-09-30. Partial Google Scholar retrieval. Scopus title queries and ACM Full-Text Collection title queries were executed on 1 October 2026. Additional-candidate screening is incomplete. ACM Guide to Computing Literature was not searched. |
| Eligibility | Matching title predicate, relevant sharing scope, verifiable date/version, and accessible primary evidence of an identifiable proposed workflow or mechanism. Empirical validation of all announced guarantees is not a filter. |
| Source genres | Conceptual proposals, prototypes, journal/conference articles, commentaries proposing a concrete workflow, and explicitly identified preprints are distinguished by their source and evidence. Secondary reviews enter Related Work, not the application denominator. Source availability or eligibility is not endorsement of all claims. |
| Decisions | The 50 original observed records retain their own denominator. The additional dated database exports have separate retrieval/consolidation counts. Current dispositions for the original 50 Scholar observations are in `protocol-search-records.csv` and `protocol-retrieval-status.json`; later export decisions are in `search-completion-candidates.csv`; the follow-up assessment is in `update-assessment-2026-10-01.csv`. Pending access/assessment is distinct from completed exclusion. |
| Assessment ordering | Initial full-text checks prioritized accessible sources and topics under revision. This pragmatic ordering can influence a partial update and was not an additional inclusion criterion. |
| Extraction | Year, application, approach/contribution, platform, reported implementation, primary locations, evaluation scope, and limits for recent records. The additive `source_table` field identifies the exact manuscript table. |
| Synthesis | Operations, actors, control objects, enforcement points, trust, and reported evidence support G1–G8. The matrix's selection was retrospective and source-specific; it does not uniformly recode all included applications. |
| Coding and inference audit | The retrospective codebook specifies the analytical unit, evidence categories, missing-information rules, and permissible inferences. Eight derivations retain paired sources and restricting cases. |
| Internal consistency checks | The visible requirement rows cite the same application pairs as the derivation register. Additional association counts remain supplementary; retention of a link does not establish inference validity after losing a premise. |
| Contextual expansion | Official policy standards and foundational output-privacy/provenance sources test interpretation of existing boundaries. They are separately documented, not an exhaustive second search or application additions. |
| Regulation | Technical responsibility, supervisory evidence, and corrective-action questions under the data-protection instruments discussed, with a targeted EUDI wallet comparison. No broad legal review or compliance certification. |
| Permitted inference | Source-specific design contrasts, derived requirements, and proposed evaluations. No new proof, experiment, global ranking, or quantitative frequency of complete integration. |

Current application counts are generated in `../output/dataset/survey-dataset-2026-10-01/counts.json`. The initial 98 historical and eight supplementary identities are preserved. Further eligible applications result from assessment of the same observed records; usefulness to the thesis, FHE, and QoE are not additional eligibility conditions.

## Synthesis and thesis contribution

`synthesis-evidence-method.md` and `synthesis-evidence-matrix.csv` trace requirements to primary locations and identify full text, indexed text, preview, inherited evidence, and unverified details. `contextual-evidence-expansion.md` explains the bounded extension. It separates identity from authority, current authorization from key/result release, confidentiality from correctness, audit integrity from completeness, withdrawal from previous disclosure, repeated-output privacy, and input provenance from truth.

The 2 October 2026 audit adds `synthesis-codebook.md`, `requirement-derivation.csv`, and internal consistency checks in `audit_synthesis.py`. It uses the existing extraction, keeps source-access statuses unchanged, and does not introduce a new application filter. The eight derivations retain application pairs, primary locations, assumptions, and restricting cases. The manuscript brings worked comparisons before the descriptive catalogue and defines when each G1-G8 question applies. The 136-record inventory remains distinct from the 50-application analytical subset and 17 contextual sources. The additional unassessed search exports remain outside these sets; their retrieval counts are supplementary.

The thesis Discussion applies these requirements retrospectively to Articles 1 and 3. Its primary role is refinement and interpretation of RQ2, with complementary audit/integrity roles for RQ1/RQ3. It preserves qualification RQs and distinguishes functional tests, conditional formal results, and secure-deployment evidence. It does not independently confirm a hypothesis, replace the QoE survey, or assign a new article number by default.

## PRISMA and reviewer limitations

The chosen designation does not claim PRISMA compliance. The justification is correspondence between the comparative objective, documented procedure, and inference scope—not a claim that PRISMA would require discarding existing studies. `prisma-and-regulatory-assessment.md` preserves that discussion.

No independent human double screening, inter-rater agreement, complete historical decision reconstruction, or exhaustive three-database update was performed. Expanding source-linked synthesis and completing accessible candidate assessments does not resolve those activities by declaration. Reviewer items remain partial/pending where the requested evidence or procedure is absent.

## Proposed wording for the response to reviewers

> We have clarified the manuscript as a structured qualitative survey of blockchain-assisted data sharing. Its contribution compares dependencies between confidentiality, consent decisions, identity disclosure, access and release enforcement, and accountability. The historical collection is preserved and the supplementary update is reported separately, with explicit title predicates, eligibility criteria, extraction fields, primary locations, source versions, and observed decisions. A source-linked synthesis matrix distinguishes conceptual mechanisms, reported evaluations, and analytical implications. We do not claim exhaustive retrieval or PRISMA compliance: historical screening records remain incomplete, retrieval is partial, and unresolved access/assessment is reported as pending. These limitations constrain the findings to documented design contrasts and assessment requirements, rather than prevalence estimates or a uniform ranking.

This wording is for author review and has not been sent to any reviewer or external service.
