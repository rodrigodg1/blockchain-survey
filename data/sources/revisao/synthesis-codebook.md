# Coding and inference rules for the qualitative synthesis

Date: 2 October 2026. This codebook documents and checks the current retrospective synthesis. It is not a prospectively registered selection protocol. It uses the retained extraction and its primary-source locators; it does not claim a new independent full-text review.

## Analytical unit and source selection

The analytical unit is the sharing or processing operation described in a source, including the actors, protected information, decision, enforcing component, and observable result. A paper can describe several operations. One matrix row summarizes a source and its relevant operations; row counts therefore cannot estimate frequencies of operations or mutually exclusive capabilities.

The fixed audit set contains the existing 50 application examples and 17 contextual sources. It includes all 38 additions and 12 initial examples used in the synthesis. This set was assembled retrospectively. The remaining 86 initial records were not uniformly coded as satisfying or failing the eight design requirements. Use of FHE and a specific application sector are not eligibility requirements.

The comparison retains contrasts in the enforcing component and checked relation: purpose queries, access tokens, policy gateways, credential verification, key release, encrypted processing, predicate proofs, and audit/correction. These contrasts justify the operation-based comparison within the selected set. They do not establish representative sampling or saturation of the literature.

## Research-question alignment

The three manuscript RQs reorganize the retained observations; they do not change application eligibility, source membership, access status, or the level of evidence.

| RQ | Comparison attributes | Existing evidence and manuscript tables |
|---|---|---|
| RQ1: Protection | Operation; named construction; protected and exposed information; cryptographic, participant, hardware, and custody assumptions. | Operation, reported mechanism, control object, trust assumptions, and source limit; protection-function and platform comparisons. |
| RQ2: Authorization and enforcement | Credential or permission record; scope/state; approving actor; on-chain/off-chain enforcing component; data/key custody; permission-change action. | Actor, control object, enforcement point, reported mechanism, and trust/limit fields; application-control comparison. |
| RQ3: Verification and evidence | Checked relation; verifier/auditor; observed events; evaluation type, operation, and scope; claims not established. | Mechanism, evaluation, evidence, trust, and limit fields; application-control comparison and requirement derivations. |

Attributes remain unextracted or unverified where the retained source material does not establish them. No new algorithm, key flow, decentralization score, measured defect, or uniform assessment of the 136 included works is inferred. The compact tables summarize selected contrasts; they are not a new full-collection coding matrix.

The rq_ids column in requirement-derivation.csv links assessment criteria to the questions they inform. Multiple links reflect different uses of a criterion, not independent findings or capabilities satisfied by an application. RQ1 concerns a protection target, RQ2 the authority and gate governing an action, and RQ3 the checked relation and its evidence. These analytical purposes can use the same source without treating their answers as interchangeable.

## Coding rules

The six compact application comparisons are retained in rq-application-comparisons.csv with their existing matrix IDs, citation keys, source versions, locations, and access statuses. The file adds table summaries, not new primary observations or application records. The preparation-stage audit checked its identifiers and locators against the matrix and its citation set against the manuscript table. The public builder checks membership against the recorded manuscript snapshot.

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

1. Each detailed application claim must identify its matrix row and primary location. The derivation register links observations to requirements, conditions, and analytical test cases.
2. Preview-only, inherited unreverified, and unavailable sources cannot supply new algorithm-level, key-flow, benchmark, or deployment claims. They can retain study identity and claims actually supported by the accessible passage.
3. A missing measurement is described as unreported or unextracted within the examined material. It is not a failed test. An analytical counterexample is a conditional case, not an observed attack.
4. Quantitative comparisons require the same defined operation and comparable workload and assumptions. The present synthesis does not pool heterogeneous measurements or rank effectiveness.
5. A requirement can be useful without being new. Earlier policy-enforcement, data-sovereignty, and governance treatments remain credited. Application-grounded assessment consequences are the analytical output.

## Contrasting cases and inference checks

`requirement-derivation.csv` records eight explicit chains from source observations to an assessment question. Each chain includes an alternative explanation or condition that restricts the inference. For example, a trusted processor need not receive the same independent-result check as a malicious processor; recipient copying prevents interpreting future access denial as recall; and absent event capture prevents interpreting log integrity as complete audit coverage.

Each question applies when the examined workflow claims the corresponding property. The register's application pair must be cited in the corresponding manuscript row. These pairs ground interpretation of the selected examples; they do not validate a universal requirement or establish independence among G1-G8.

These cases are drawn from the retained extraction and its source-specific evidence records. They are checks against overgeneralization within the selected examples, not an independent search for all counterexamples in the literature. No new source membership, source-access status, or empirical finding is created by the codebook.

## Source-dependence checks

During manuscript preparation, the synthesis audit recomputed requirement links under five views: all 50 application examples; the 44 with direct or assessment-stage full-text checks; the 35 with direct full-text checks; their 28 recent examples; and their seven historical examples. The last three exclude preview, indexed-only, inherited-unreverified, unavailable, and assessment-only rows as applicable. Contextual sources are excluded from all five application denominators.

The audit also removed each directly checked application row in turn and recorded whether every requirement retained another application link. This checks stored associations. A remaining link does not show that an inference remains valid after losing one of its premises, or that the remaining source provides equivalent evidence. It does not estimate statistical reliability, prove independence of findings, validate the extractions, or certify that an application satisfies a requirement. In particular, the inference/composition question in G7 retains its separately identified theoretical conditions. The manuscript reports the derivation conditions. Association counts are consistency diagnostics, not additional findings or application evaluations.

## Completion boundary and remaining work

The finite analytical audit is complete when every current matrix row has an identifiable source, role, access status, operation, source location, and evidence limit; every requirement has an explicit derivation and restricting case; and the specified source-dependence checks have run without inconsistencies. This is an audit completion rule, not a literature-search stopping rule or evidence of saturation.

Additional retrieval and screening have a separate boundary. The original 50 assessed observations, the 136 included applications, and the 817 consolidated additional candidates remain distinct. The latter contain 781 records awaiting title/abstract screening and 36 duplicate-current-application dispositions. Missing primary text remains pending. No access failure is converted into a scientific exclusion.

Complete screening of the additional candidates, broader abstract/keyword retrieval, independent human assessment, and reconstruction of the unavailable historical decisions have not been performed. The first three would support broader coverage or extraction-confidence claims; they are not automatic prerequisites for the bounded qualitative comparisons. Historical decisions cannot be recreated without contemporaneous evidence. The present audit supports design contrasts and conditional assessment questions, not exhaustive coverage or field-wide unsolved-problem claims.
