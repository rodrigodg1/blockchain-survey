# Consent and data provenance in sports analytics

This publication is classified under consent management. The source evidence below covers the reported workflow and the scope of its evaluation.

## Primary source and retrieval

Ferreira, Joao C, and Frederica Gonçalves. *Blockchain-enabled Model Context Protocol (MCP) for trust and consent in LLM-orchestrated sports analytics*. Journal of Sports Analytics 12 (2026). [Publisher version](https://journals.sagepub.com/doi/10.1177/22150218261448184), DOI 10.1177/22150218261448184. First online 25 May 2026, verified against publisher HTML and Crossref metadata. Publisher HTML was accessible in the browser; direct HTTP/PDF retrieval failed. Relevant methods, evaluation, discussion, tables and pseudocode were inspected in the primary HTML, not inferred from the abstract. No executable experiment repository was identified in the inspected text.

The publication was identified through title query S04. The query and source locators are listed in the protocol and the corresponding evidence records.

## Eligibility against the existing rules

| Rule | Evidence and decision |
|---|---|
| Original title predicate | Title contains blockchain and consent; native S04 retrieval confirmed. |
| Publication period/version | Publisher journal article, first online 25 May 2026; within the update interval and cutoff. |
| User-data scope | Athlete telemetry, injury records and performance data shared with coaches, medical personnel and scouts. Synthetic evaluation does not remove the designed user-data use case. |
| Primary operation/control description | Methodology, Tables 3–4 and use-case workflows describe credential scope/status checks before MCP retrieval, wallet-held credentials and hash-anchored result bundles. |
| Existing classification | Consent: data-category, purpose, time-window and recipient permissions. DIDs/VCs are supporting mechanisms; no second classification or agentic-AI category is needed. |
| Duplicate handling | Distinct DOI and sports-domain report. Related to the already included MCP/FHIR report; no claim of independent replication or pooled empirical support. |

## What the source supports

The Methodology section, Tables 3–4, and Appendix 1 describe an MCP access pipeline with credential and consent checks, canonicalized bundle hashes, off-chain data, and provenance records. Table 3 states a permissioned consortium/BFT design, institutional issuers, athlete-held wallets and query-time enforcement. The described controls provide an application example for existing G1, G2, G5, G6 and G8. They are not coded as verified satisfaction of those criteria.

The Evaluation section reports synthetic data for 500 athlete profiles, 40 performance metrics and 20,000 transactions, and states 30 runs. These are source-reported design/evaluation details, not independently reproduced results. Table 8 and the threat-model discussion explicitly distinguish provenance from semantic correctness of LLM outputs. Table 9 identifies privacy-breach reductions, health outcomes and operational benefits as prior-literature or hypothetical outcomes rather than this prototype's measurements. The survey does not repeat those benefits as demonstrated results.

## Evidence limitations that must survive incorporation

- **Metric ambiguity:** Tables 5–6 report 96.8% provenance verification, while Table 8 reports 100% for a baseline synthetic workload; the text does not provide a reconciled mapping between workloads and these outcomes. The metric definition alternates between successful hash matches and correct tamper/validity decisions. No comparative performance conclusion is imported.
- **Issuer ambiguity:** Tables 3–4 assign credential issuance to trusted institutions, while the use-case workflow and sample credential describe athlete issuance. Athlete approval, holder control and issuer authority must not be treated as interchangeable.
- **Deployment/finality ambiguity:** Table 3 describes finality-based consortium consensus, whereas Challenges reports simulated two-block reorganizations. Future Work still calls for experimentation with concrete permissioned infrastructures. The extracted platform remains a stated consortium design; no specific production deployment is asserted.
- **Revocation boundary:** Challenges reports rejection after withdrawal and cache invalidation on the next validation cycle. This does not establish immediate propagation to every recipient, deletion of disclosed information, or safety under all compromised-endpoint/collusion conditions.
- **Verification boundary:** Hash integrity and authentic provenance do not establish truthful measurements, complete event capture, correct analytics, or a correct LLM-generated explanation. Optional ZKPs are mentioned without an evaluated construction that could establish confidential processing.
- **External validity:** Synthetic workload and exploratory subgroup comparisons do not establish field effectiveness, fairness, user understanding of consent or legal compliance.

## Relationship to the MCP/FHIR report

The existing extraction for [Ferreira et al., MCP/FHIR](https://doi.org/10.1109/ICDLT66400.2025.11466653), matrix SC07, identifies gateway checks, issuer allowlists, purpose/time permissions, bundle hashes and revocation-cache assumptions (IV.A–F; V.D/Table 3; VI). The sports paper shares an author and this architectural pattern. It describes different application workflows and a different reported synthetic workload; these justify retaining a separate publication in the publication inventory. They do **not** establish independent replication, independent implementation, or absence of all textual/design overlap. A forensic duplication/plagiarism assessment was not performed. No effect sizes are pooled and no conclusion depends on treating these as two independent demonstrations.
