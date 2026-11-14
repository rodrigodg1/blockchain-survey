# Source-linked derivation of the qualitative synthesis

The survey classifies 139 publications: 48 on privacy protection, 59 on consent management, and 32 on decentralized identity. Its qualitative synthesis compares selected data-sharing operations involving multiple stakeholders, examining participating entities, permission-enforcing services, data and decryption-key custody, recipient disclosure, and reported evaluations. The evidence matrix records source locators, described operations, and reported conditions for these comparisons. Differences in study scope, reporting, and source access limit which dimensions can be compared. Each comparison identifies its supporting publications; no uniform depth of extraction is implied across the collection.

## Extraction and source access

Three research questions govern interpretation. RQ1 covers privacy, consent, and selective sharing; RQ2 covers individual identity control; RQ3 covers enabling platforms and protocols. Verification and governance remain complementary dimensions. The codebook and `rq_ids` in `requirement-derivation.csv` use these meanings.

The retained access records for two Scopus applications assessed on 26 October 2026 distinguish DB1's indexed publisher sections from DB2's accessible primary HTML. These source-specific assessments do not establish completion of candidate screening or uniform access to the collection. Their access limits remain attached to the observations used in each comparison.

Each CSV row records a citation key and collection role; primary URL and examined version; exact section, figure, theorem, or page locator where verified; access status; operation, actors, control object and enforcement point; reported mechanism and evaluation; evidence type; trust assumptions and limits; derived requirement IDs; and an analytical counterexample or boundary. Page locators distinguish printed pages from PDF positions. An author proof, arXiv manuscript, living specification, and publisher version of record are identified separately. The AnonCreds living specification has an access date but no pinned commit; this limits exact replay of that row.

Primary papers were checked through publisher, author-hosted, author-deposited, institutional, or NCBI BioC text. Standards were checked against official publications. DOI metadata for the two added theoretical works were checked separately from their primary text. Search-indexed publisher sections provide a more limited basis than a successfully retrieved complete document. No missing mechanism, key sequence, performance configuration, or assumption is filled from architectural plausibility.

The access statuses have distinct meanings:

- `primary_fulltext_verified`: relevant passages were checked in an accessible primary document. This does not indicate independent reproduction or verification of every statement in the source.
- `primary_fulltext_verified_via_assessment`: the eligibility-assessment stage examined complete primary text, and this synthesis row uses its source-specific extraction and locators. Additional role or trust details not established by that record remain marked as unverified or not separately extracted. This is not independent human double coding.
- `primary_indexed_sections_verified`: the specified publisher sections were accessible through indexed text; the complete direct download was unavailable.
- `primary_local_text_verified`: a preserved local primary text was checked after the current web retry failed.
- `primary_preview_only`: only the explicitly located abstract or publisher preview was verified. Detailed algorithms, trust models, and evaluations remain `not_verified` where unavailable.
- `retained_extraction_not_reverified`: an existing extraction/reference is retained, but primary full text was not recovered during this audit. No new detailed inference is supported by the current abstract alone.
- `retained_legal_reference_not_reverified`: an existing article-level legal mapping is retained after a current access challenge; no new legal interpretation is added.
- `not_verified`: the relevant primary material was not obtained. The row preserves the bibliographic/thematic reference and marks unavailable details.

## Derivation and limits of interpretation

Evaluation objectives are linked to specific boundaries rather than to paper counts. G1 separates identity evidence and decision authority. G2 connects scope and current authorization to enforcement. G3 identifies key custody and release authority. G4 identifies the verified relation and separates confidentiality, correctness, and release permission. G5 distinguishes record integrity, event capture, review disclosure, responsibility, and corrective authority. G6 examines propagation of withdrawal and status. G7 examines linkability and inference across repeated interactions and outputs. G8 distinguishes input provenance from factual truth.

For each source, the derivation first identifies the operation actually described or evaluated, then the responsible component and information it controls, and finally a limit that the reported evidence does not cross. The manuscript's evaluation-objectives table presents supporting application observations alongside the corresponding assessment question. It connects privacy, consent, and verification within the application operation. Regulations and standards interpret scope, accountability, and obligations without adding application results or establishing compliance.

G1 uses Seidi's separate role permissions. G6 uses DualCare's key removal and Kang's URL expiry, with Ramirez's issuer revocation as an additional credential-status example. G7 links Liu's retained credential-use identifiers (SC13) and Hussain's incompletely specified privacy accounting (SM38) to assessment of linkability and disclosure across repeated interactions. The matrix also retains Zeydan's credential and authentication observations with their source-specific limits. These observations do not establish measured leakage attacks. The manuscript identifies the sources supporting each comparison and objective.

Evidence types are descriptive categories, not a validated numerical quality score. A formal definition, local simulation, transaction benchmark, conceptual architecture, technical standard, and regulatory guidance support different conclusions. None is silently promoted to independent deployment evidence, complete workflow enforcement, or compliance certification.

The open-problem agenda follows the same derivation: observed evidence limit, bounded research question, then a direction and evaluation criteria. It compares comprehension and prediction (Barnes, Bonotis, Deepthika), audit evidence and correction authority (Ghosh, Lu), payload protection and interaction metadata (BADIMAC, SS-DID), and component measurements and cross-implementation workflows (Ramirez, Seidi, DualCare). Continuity during stale state, recovery, migration or service failure is a proposed evaluation, not a measured failure in these applications. Existing protocol profiles and conformance tests are contextual baselines. Partial retrieval prevents claims that the identified questions remain unsolved throughout the field.

The counterexample column records conditional analytical cases used to test an inference. It does not assert a measured attack, implementation flaw, or observed incident in the named study. For example, an expired access URL does not remove a downloaded ciphertext; a valid credential does not establish that its asserted measurement is true; and an intact log does not establish that all relevant events were recorded. These cases delimit what the cited mechanism alone establishes.

Dinur–Nissim supplies a reconstruction result under a particular database, query-access, and perturbation model. Dwork–Roth supplies differential-privacy definitions and composition results under their stated assumptions. Neither establishes that the reviewed deployments admit those attacks or implement differential privacy. The manuscript's subtraction of overlapping exact sums is a conditional mathematical example, not an experiment or a reported vulnerability of a surveyed system. The VC data model distinguishes verification from truth; PrivDA supplies a concrete source-data trust assumption. ODRL and XACML establish existing policy-expression and decision/enforcement concepts, not a new architecture invented by this survey.

This audit was prepared with automated research and extraction assistance. No independent human double coding, inter-rater reliability, exhaustive contextual search, or reproduction experiment was performed. Source-specific judgments remain reviewable through the locators and stated access limits.

## Preservation and reproducibility

The matrix records analytical notes, source URLs, examined versions, and locators. Where available, the source fingerprint identifies the examined copy. The [source snapshot](../../source-snapshot.json) records the matrix fingerprint and its inputs.

## Derivation register

`requirement-derivation.csv` records eight paired-source derivations, their exact existing primary locations, conditions, restricting cases, and proposed assessments. The pairs cover identity/authority, permission state, custody, proof relations, audit/correction, withdrawal, output inference, and input truth. A proposed assessment is not an observed failed test. The comparison credits established policy-enforcement and governance treatments and does not infer novelty from usefulness to the thesis.


## Related analyses

Related treatments establish the following control distinctions.

| Primary source and examined material | Established analysis | Consequence for this survey |
|---|---|---|
| [Ernstberger et al., Data Sovereignty](https://eprint.iacr.org/2023/967), abstract and indexed primary excerpt of section 5.1; no complete PDF inspection | Access, input, and output predicates; access controllers, compute nodes, and result consumers; computation checking and residual policy | These control distinctions are established. The contribution is their application-specific comparison against reported checks and assumptions. |
| [Sandyawan et al., Five Safes](https://doi.org/10.3390/math14163009), publisher-indexed HTML sections 3.3 and 5-6; direct publisher request failed | Governance evaluation questions include purpose, authorization, accountability, and output disclosure | Evaluation questions alone are not a distinct contribution. The survey credits this treatment when discussing evaluation objectives. |
| [Ambati et al., Self-Sovereign Digital Identities, v2](https://arxiv.org/html/2603.06896v2), primary HTML sections 2, 4.2, and 6; version dated 11 March 2026 | Identity binding, key management, revocation, and trust-infrastructure dependence | The survey uses this contextual source for the identity-control analysis. |

This is a targeted comparator check, not exhaustive novelty verification or a replacement for application screening. The manuscript does not claim new control categories, first governance evaluation questions, or independently validated design requirements.
