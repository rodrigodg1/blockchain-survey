# Bounded expansion of the qualitative analysis

## Purpose and separation of evidence

The 2026-10-01 revision expands interpretation of the sharing workflow, not the application-search predicates. The application collection remains governed by the original privacy, consent/permission, and decentralized/self-sovereign identity title predicates and the supplementary update's date, scope, version, and primary-evidence requirements. Newly completed assessments of the 50 observed records can change the number of included applications. Contextual sources below do not enter that denominator.

The analytical extension examines authorization scope and current state, key custody and release, cumulative output disclosure, input provenance, and the evidence needed for supervision. These questions also permit a retrospective application to the thesis architectures. Their usefulness to the thesis is not an inclusion criterion for application studies, and neither FHE nor QoE is introduced as a required search term.

## Documentary procedure

This is a targeted contextual check rather than an exhaustive literature search or a second systematic review. Sources were sought to test specific boundaries already raised by the comparison. Official standards and foundational research were preferred to commentary. The accompanying synthesis matrix and method record primary locations, evidence-access levels, source versions, interpretation limits, and requirement IDs. Application assessment decisions are recorded separately in `update-assessment-2026-10-01.csv`.

| Question | Source and verified location | Use and boundary |
|---|---|---|
| Does a permission expression itself identify an enforcement mechanism? | W3C *ODRL Information Model 2.2*, Recommendation 2018-02-15, Sections 2 and 2.1; https://www.w3.org/TR/2018/REC-odrl-model-20180215/ | Describes policy, asset, action, party, permission, prohibition, duty, and constraints. Used as vocabulary, not evidence that a surveyed system implements ODRL or enforces every expressible obligation. |
| How are policy decisions distinguished from access enforcement? | OASIS *XACML Version 3.0*, Standard 2013-01-22, Sections 2, 3, and 7.2; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html | Identifies policy decision and enforcement points and the latter's handling of decisions and obligations. The separation predates this survey and is not claimed as a new architectural invention. |
| Can correct authorized outputs disclose individual contributions? | Dinur–Nissim (2003) and Dwork–Roth (2014), primary locations and version metadata in `synthesis-evidence-matrix.csv` and `contextual-verification-additions.bib` | Motivates evaluation of reconstruction and composition. The manuscript's subtraction of two exact overlapping sums is an explicitly conditional mathematical example, not a reported attack or new experiment on the included systems. |
| Does successful credential verification establish a claim's truth? | W3C *Verifiable Credentials Data Model v2.0*, Recommendation 2025-05-15, Sections 1.1 and 2; existing key `bg-vc-data-model-2` | Establishes the distinction between verification and truth. A computation over authenticated inputs can remain correct while measurement quality is assumed or outside the guarantee. |

The standards were read through their official web publications on 2026-10-01. Research-paper access and source locations are documented by the evidence audit. Missing details are not supplied from architectural plausibility. Abstract or preview access supports only what that accessible passage states; it does not support detailed workflow attribution.

## Stable synthesis requirements

- G1: distinguish identity evidence from decision authority.
- G2: bind authorization scope and the current applicable state to enforcement.
- G3: identify key custody and result-release authority.
- G4: separate confidentiality from computation correctness.
- G5: distinguish audit integrity, completeness, and disclosure.
- G6: propagate withdrawal and credential-status changes to the relevant services.
- G7: assess repeated-output inference and composition.
- G8: distinguish input provenance from the truth of an observation.

These are analytical requirements and assessment questions. They are not empirical findings about prevalence, a validated taxonomy, a unified threat model for all studies, or evidence that the thesis architecture meets the complete set. The supplementary matrix provides a source-specific basis for testing the reasoning. It does not uniformly recode the historical collection.

## Preservation and thesis application

The historical 98 identities and existing eight update inclusions are preserved. The new source snapshots in `analysis-expansion-before.json` permit comparison with the state before this revision. Further eligible update studies are additive and must satisfy the same predicates; inaccessible or unresolved records remain pending rather than being counted as exclusions.

The thesis application is in [the thesis integration module](../../../thesis_defense/tex/governance_survey_integration.tex), with a separate evidence trail. It maps the requirements to Article 1 and the current developing Article 3, primarily for RQ2, and distinguishes reported mechanisms, conditional formal results, functional tests, and remaining limits. It does not change qualification RQs or claim that this developing survey historically caused the published design. The existing publication chapter structure is preserved.
