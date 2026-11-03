# Coding and inference rules for the qualitative synthesis

Updated: 26 October 2026. This codebook documents and checks the current retrospective synthesis. It is not a prospectively registered selection protocol. It uses the retained extraction and its primary-source locators; it does not claim a new independent full-text review.

## Analytical unit and source selection

The analytical unit is the sharing or processing operation described in a source, including the actors, protected information, decision, enforcing component, and observable result. A paper can describe several operations. One matrix row summarizes a source and its relevant operations; row counts therefore cannot estimate frequencies of operations or mutually exclusive capabilities.

The fixed audit set contains the existing 53 application examples and 17 contextual sources. It includes all 41 supplementary applications and 12 historical examples used in the synthesis. This set was assembled retrospectively. The remaining 86 historical applications are inventory records, not silently coded as satisfying or failing G1-G8. Relevance to the thesis, use of FHE, and QoE are not eligibility requirements.

The comparison retains contrasts in the enforcing component and checked relation: purpose queries, access tokens, policy gateways, credential verification, key release, encrypted processing, predicate proofs, and audit/correction. These contrasts justify the operation-based comparison within the selected set. They do not establish representative sampling or saturation of the literature.

## Research-question alignment

The original manuscript RQs are restored verbatim. RQ1 concerns mechanisms for privacy, consent, and selective sharing of user data among stakeholders; RQ2 concerns individual identity control; RQ3 concerns platforms and protocols enabling privacy and identity. Governance and verification are complementary attributes within these questions, not replacement RQs or inclusion filters.

Application control observations and G1–G8 primarily inform RQ1; credential, issuer, recovery, and status dependencies also inform RQ2. The separately sourced platform/identity-infrastructure comparisons answer RQ3. RQ identifiers in `requirement-derivation.csv` refer to these original questions. The original three classifications and 98 historical memberships are unchanged. The two added Scopus records use the original privacy title predicate and user-data-sharing scope; one has indexed primary sections only. They are outside the original 50 Scholar observations.

Attributes remain unextracted or unverified where source material does not establish them. A performance measurement does not broaden a proof's statement or an audit's observed events. The 139 records are not uniformly evaluated against G1–G8, and source availability does not establish scientific validity.

## Coding rules

The six compact application comparisons are retained in rq-application-comparisons.csv with their existing matrix IDs, citation keys, source versions, locations, and access statuses. The file adds table summaries, not new primary observations or application records. Internal checks compare its identifiers and locators with the matrix and its citation set with the manuscript table.

| Field or decision | Rule |
|---|---|
| Operation | Identify the requested action and information affected. Do not infer a complete workflow from a component benchmark. |
| Actor and authority | Separate requester authentication, issuer assertions, permission to approve, processor responsibilities, custody, recipient, and reviewer. One organization can hold several roles. |
| Control object | Name the record, credential, policy, key, output, or event population. Revocation of one object is not automatically revocation of the others. |
| Enforcement point | Identify the component that allows or rejects the action. A ledger entry or policy expression is not itself evidence of enforcement at an external service. |
| Checked relation | Name exactly what a signature, hash, credential check, proof, or audit compares. Do not promote it into a different relation. |
| Reported evaluation | Record the tested operation, workload/configuration where extracted, and metric. Keep proposed behavior separate from observed behavior. |
| Trust and limits | Retain source-specific trust, custody, input-origin, event-capture, and deployment assumptions. Omitted information is an extraction/access limit, not a demonstrated system defect. |
| Source access | Preserve the matrix's access status. Full text means relevant passages were checked, not independent reproduction. Assessment-derived records are distinct from direct synthesis checks. |
| Requirement assignment | A G1-G8 link identifies a boundary relevant to the assessment question. It does not mean that the source satisfies the requirement or fails a test. Multiple links per source are permitted. |
| Contextual source | Use theory, standards, and legal guidance to define an interpretation or condition. Do not count them as application evaluations or certification. |

Three evidence categories govern prose: a source describes or proposes a control; a source reports an evaluated behavior or a result under assumptions; the survey derives a conditional assessment question. Access status and evidence category are separate. A complete conceptual paper remains conceptual evidence.

## Claim-admissibility rules

1. Each detailed application claim must identify its matrix row and primary location. The supplemental derivation register links observations to requirements, conditions, and analytical test cases.
2. Preview-only, inherited unreverified, and unavailable sources cannot supply new algorithm-level, key-flow, benchmark, or deployment claims. They can retain inventory identity and claims actually supported by the accessible passage.
3. A missing measurement is described as unreported or unextracted within the examined material. It is not a failed test. An analytical counterexample is a conditional case, not an observed attack.
4. Quantitative comparisons require the same defined operation and comparable workload and assumptions. The present synthesis does not pool heterogeneous measurements or rank effectiveness.
5. A requirement can be useful without being new. Earlier policy-enforcement, data-sovereignty, and governance treatments remain credited. Application-grounded assessment consequences are the analytical output.

## Contrasting cases and inference checks

`requirement-derivation.csv` records eight explicit chains from source observations to an assessment question. Each chain includes an alternative explanation or condition that restricts the inference. For example, a trusted processor need not receive the same independent-result check as a malicious processor; recipient copying prevents interpreting future access denial as recall; and absent event capture prevents interpreting log integrity as complete audit coverage.

Each question applies when the examined workflow claims the corresponding property. The register's application pair must be cited in the corresponding manuscript row. These pairs ground interpretation of the selected examples; they do not validate a universal requirement or establish independence among G1-G8.

These cases are drawn from the retained extraction and its source-specific evidence records. They are checks against overgeneralization within the selected examples, not an independent search for all counterexamples in the literature. No new source membership, source-access status, or empirical finding is created by the codebook.

## Source-dependence checks

`audit_synthesis.py` recomputes requirement links under five views: all 53 application examples; the 46 with direct or assessment-stage full-text checks; the 37 with direct full-text checks; their 30 recent examples; and their seven historical examples. The last three exclude preview, indexed-only, inherited-unreverified, unavailable, and assessment-only rows as applicable. Contextual sources are excluded from all five application denominators.

The audit also removes each directly checked application row in turn and records whether every requirement retains another application link. This checks stored associations. A remaining link does not show that an inference remains valid after losing one of its premises, or that the remaining source provides equivalent evidence. It does not estimate statistical reliability, prove independence of findings, validate the extractions, or certify that an application satisfies a requirement. In particular, the inference/composition question in G7 retains its separately identified theoretical conditions. The manuscript reports the derivation conditions. Association counts remain audit records and are not presented as findings about requirement satisfaction or field prevalence.

## Completion boundary and remaining work

The finite analytical audit is complete when every current matrix row has an identifiable source, role, access status, operation, source location, and evidence limit; every requirement has an explicit derivation and restricting case; and the specified source-dependence checks have run without inconsistencies. This is an audit completion rule, not a literature-search stopping rule or evidence of saturation.

Additional retrieval and screening have a separate boundary. The original 50 assessed observations, the 139 included applications, and the 817 consolidated additional candidates remain distinct. The latter contain 777 records awaiting title/abstract screening, two retained Scopus applications, two pending primary texts, and 36 duplicate-current-application dispositions. Missing primary text remains pending. No access failure is converted into a scientific exclusion.

Complete screening of the additional candidates, broader abstract/keyword retrieval, independent human assessment, and reconstruction of the unavailable historical decisions have not been performed. The first three would support broader coverage or extraction-confidence claims; they are not automatic prerequisites for the bounded qualitative comparisons. Historical decisions cannot be recreated without contemporaneous evidence. The present audit supports design contrasts and conditional assessment questions, not exhaustive coverage or field-wide unsolved-problem claims.

The targeted S04 follow-up on 26 October 2026 adds one consent application (FU01), with primary HTML checked and the same eligibility criteria. It is outside the original 50 observations and 817 exported candidates. See `sports-analytics-assessment-2026-10-26.md`. No agentic-AI criterion, class, or RQ is introduced; the related FHIR and sports reports are not treated as independent replication.
