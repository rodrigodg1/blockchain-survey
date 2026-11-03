# Survey revision: evidence and thesis contribution

Assessment date: 26 October 2026. Canonical manuscript: `../main.tex`; compiled artifact: `../output/pdf/main.pdf`. This record explains the revision; it is not a certification of search completeness or cryptographic security.

## Preserved scope and methodological limits

The three survey questions are restored verbatim from `previous-submission-ACM/ACM Version - Blockchain Survey/main.tex`. Their roles remain mechanisms for privacy/consent/selective sharing (RQ1), individual control of decentralized identity (RQ2), and enabling platforms/protocols (RQ3). Governance and verification are complementary analytical dimensions, not replacement RQs or new eligibility gates. Application classifications remain privacy, consent, and decentralized identity.

The researcher clarified that eligibility involves use of users' data. This clarification is now explicit. It does not retrospectively reconstruct undocumented historical decisions. The nine title queries, three databases, original classifications, and publication cutoff of 30 September 2026 are preserved. Platform documentation checked on 26 October is a separate technical snapshot, not an extension of the publication cutoff. No original exclusion log or independent human screening was invented.

The collection contains 138 publications: the same 98 historical identities and group assignments, plus 40 update records. Group totals are 48 privacy, 58 consent, and 32 identity; historical totals remain 40/33/25. The detailed synthesis contains 52 application publications (40 recent, 12 historical), with 17 interpretive sources outside the application count. Forty-five of the 52 have direct full-text checks or source-specific full-text assessments; seven retain limited-source caveats. These categories describe source access, not independent security validation or study quality.

The original 50 assessed Google Scholar observations still account for 38 inclusions, one pending text, three scope exclusions, and eight other dispositions. Two additional inclusions come from Scopus S02 and must not be added to that denominator:

| Study | Evidence used | Bounded contribution |
|---|---|---|
| Hu et al., *Invisi-Reveal* (2024), [10.1016/j.jisa.2024.103866](https://doi.org/10.1016/j.jisa.2024.103866) | Publisher-indexed abstract/introduction; direct full text restricted | Anonymous request authentication and conditional traceability. No new algorithm-level or performance inference. |
| Ren et al. (2024), [10.1016/j.jksuci.2024.101969](https://doi.org/10.1016/j.jksuci.2024.101969) | Accessible primary article, especially sections 4.1, 6, and 7 | Distinguishes distributed key custody from a protocol in which the authorized recipient ultimately reconstructs a master secret. A local Ganache evaluation does not establish independent deployment or independently validated security. |

The additional exports contain 843 observations consolidated to 817 candidates: 36 inventory overlaps, two inclusions, two pending primary texts, and **777 awaiting screening**. The two pending ACM papers have DOIs `10.1145/3640115.3640188` and `10.1145/3659463.3660027`; direct publisher access returned 403. These are not exclusions. The original pending Scholar chapter, `10.1007/978-3-031-60221-4_42`, also remains unresolved. Scopus exports cover the observed S02/S05/S08 result sets; ACM covers its Full-Text Collection, not the Guide to Computing Literature. Scholar pagination remains incomplete. Screening order prioritized mechanisms under revision and can bias an unfinished update.

**The bibliographic update is not complete.** The manuscript explicitly presents a bounded qualitative comparison. Remaining retrieval and screening must be completed before claiming comprehensive updated coverage. Neither the automated checks nor this revision supplies analytical saturation, prevalence estimates, an effectiveness ranking, or proof of methodological equivalence where historical records are unavailable.

## Platform decisions

`platform-candidate-assessment-2026-10-26.csv` records all 18 platform/tool candidates and three network candidates in the student's PDF, plus Arcium and Oasis Sapphire as additional comparators. `platform-update-sources-2026-10-26.csv` records new source checks; existing citation keys resolve in the bibliography. These sources do not increase the application denominator.

- The original eight protocol rows remain: Zcash, Tornado Cash, Incognito, Aztec, Monero, Secret Network, Grin, and Beam. Incognito is explicitly legacy context with current deployment unverified.
- Eleven protocol rows were added: RAILGUN, Privacy Pools, Aleo, Namada, Midnight, Dusk, Zama, CoFHE, Inco, Arcium, and Oasis Sapphire. This is a selected comparison of 19 protocols, not a platform census.
- Kohaku is discussed as wallet/SDK tooling, not counted as a blockchain protocol. Tor and I2P remain network context; Nym was added at that boundary.
- The paper distinguishes Inco Lightning's TEE architecture from an FHE roadmap; Phoenix's documented design from its paused new-transaction admission; and threshold key services from both replicated computation and succinct correctness proofs. CoFHE descriptions are explicitly tied to the architecture updated on 20 April 2026, not every later SDK deployment mode.
- Launch/token speculation, blanket energy/throughput judgments, market-share claims, unverified exploit chronology, and legal-news assertions from the PDF were not adopted. A protocol was not excluded merely because an attached claim about it was unsupported. ZK proofs are not classified as inherently Layer 2, and association-set membership is not equated with legal compliance.

## Specific contribution to the thesis

The canonical thesis RQs in `../../../qualification/metadata.yaml` concern auditable encrypted QoE history (RQ1), granular individual control over entities computing on data (RQ2), and independent confirmation of the computation sequence/results (RQ3). They are distinct from the survey's RQs. The thesis foundation, findings map, board analysis, article-gap map, current manuscripts, researcher inputs, and knowledge-base context were used to check the connection.

| Thesis issue not fully settled by existing articles | What this survey contributes | Boundary and complementarity |
|---|---|---|
| What does granular user control actually govern: retrieval, computation requests, or result release? | A source-linked distinction between these operations, their recipients, enforcing components, policy versions, and key holders. | Directly informs thesis RQ2 and evaluation criteria. It does not demonstrate that the PoC's ACL controls every possible computation on public ciphertexts. |
| Which trust assumptions remain after selecting FHE and a blockchain? | Comparison with client-side proofs, MPC, TEEs, credential services, and data/key-release mechanisms. | Supplies DSR requirements and rationale under an explicit threat model. It does not rank FHE above alternatives without a controlled workload/utility comparison. |
| What do consent records, credential authenticity, and verified computation establish about a sensitive-data workflow? | Separates evidence of permission, issuer statements, recorded actions, correct computation, input truth, and released-output privacy. | Helps interpret thesis RQ1/RQ3. It does not solve truthful measurement, cumulative output inference, auditor participation, private availability, or independent deployment. |
| How should withdrawal, identity recovery, and status changes reach downstream services? | Identifies dependencies between current policy and repositories, issuers, wallets, caches, tokens, and key services. | Provides assessment questions for multi-stakeholder designs; the survey is not a new implementation or experimental answer. |

Article 1 (published QoE PoC, DOI `10.1145/3772072`) demonstrates an application workflow with FHE and access control; its replicated execution must not be described as an absence of verification. The present survey contributes a broader comparative vocabulary for specifying what such controls authorize and which actors still obtain plaintext or keys.

Article 2 (published QoE survey, DOI `10.1016/j.comnet.2025.111899`) organizes application-specific QoE approaches. The present survey compares cross-domain user-data sharing, consent, identity, and enforcement boundaries. Its contribution is complementary only if these operation-level comparisons remain central; repeating the QoE survey or claiming it established universal FHE superiority would create redundancy or unsupported positioning.

Article 3's current source is `../../article_3-acm/acm-version-verificar/main.tex`. It supplies the thesis's computation-verification construction and bounded implementation evidence. The present survey helps specify the guarantees that this construction must be assessed against; it supplies no additional validation of that construction. In particular, functional Test-parameter results do not establish secure-profile confidentiality, and reduced replay redundancy does not establish end-to-end verification cheaper than one recomputation.

Within DSR, the survey therefore supports problem characterization, requirements derivation, and retrospective interpretation of artifacts. Its independent scientific output is the comparative synthesis linking privacy mechanisms and identity/consent decisions to concrete disclosure and enforcement boundaries. The manuscript states this without introducing thesis-specific experiments or forcing QoE into the survey's eligibility criteria. The source-dependence audit checks traceability of the eight conditional assessment criteria; it does not establish that they are necessary, sufficient, exhaustive, or independently reproduced.

## Submission condition and repository boundaries

The manuscript and bibliography were edited directly. RQ wording, historical identities/classifications, count consistency, citations, references, compilation, and PDF layout are checked by the revision artifacts. Compilation success is not scientific certification.

Author contributions, competing interests, and the author-approved AI-use statement remain deferred at the researcher's request. No claims about coauthorship, conflicts, or completed human verification were fabricated.

The public companion repository has not been synchronized or published by this revision. Its release must match the revised local evidence before submission. The manuscript's Data availability statement makes that condition explicit. The local submission archive is a review package, not a declaration of submission readiness.

Navigation and state verification found older survey counts/title in project documentation and references to the previous Article 3 path in repository state. Some thesis notes also retain an overbroad 'FHE shield' interpretation. Those files were not updated because the user's write scope is the survey and directly necessary evidence. The revision changes no thesis chapter plan or repository routing. Published papers, the qualification baseline, and unrelated working-tree changes were preserved.
