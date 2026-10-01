# Primary-text assessment for the search completion

Assessment date: 1 October 2026. Publication cutoff: 30 September 2026. Full-text inspection of these search candidates is authorized by the researcher. Inclusion records below require matching extraction, bibliography, and manuscript updates before they enter the application-study count.

## Ghosh, Mukhopadhyay, and Chakraborty: open banking

Primary publication: [Design and Architectural Implementation of Consortium Blockchain Based Framework for Open Banking Customer Consent and Data Handling](https://doi.org/10.1007/s42979-023-02593-4), *SN Computer Science* 5, 271. Published 15 February 2024. Original observation: S04, rank 14, page 2. Decision: eligible application study, consent group.

The full 19-page publisher PDF was accessed through the USP subscription. Pages 7–13 describe the bank, third-party provider, customer, and regulator workflow. A bank-side consent database and gateway check sharing requests. Corda transactions record the agreement and the reported exchange. A regulator-owned notary checks agreement status and a supervisory component compares authorized fields with reported shared fields. Customers can receive violation notifications and revoke consent.

The reported proof of concept uses Corda Enterprise 4 and bank emulation with GlassFish. Figures 6–8 show the implemented workflow. Table 3 on page 16 reports execution times for 4, 6, 8, and 10 nodes with customer-count parameters from 10 to 50. Reported times range from 625 to 9,424 ms. These observations do not establish performance beyond the evaluated configurations. The STRIDE discussion on pages 14–17 is a qualitative threat analysis, not a cryptographic security proof. No public project repository was identified in the inspected text.

The supervisor can compare exchanges recorded by participating gateways. The paper does not establish that all out-of-band transfers are logged, that recipients delete released data after withdrawal, or that a notary proves downstream purpose compliance. Claims equating enclaves with homomorphic encryption or zero-knowledge proofs are not adopted. Evidence supports G1 (authorization scope), G2 (enforcement boundary), G5 (audit completeness), and G6 (withdrawal).

## Guan, Cao, and Zhang: healthcare IoT

Primary publication: [Blockchain-Enhanced Data Privacy Preservation and Secure Sharing Scheme for Healthcare IoT](https://doi.org/10.1109/JIOT.2024.3487154), *IEEE Internet of Things Journal* 12(5), 5600–5614. First published 28 October 2024, final issue 1 March 2025. Original observation: S01, rank 7, page 1. Decision: eligible application study, privacy group.

Institutional authentication enabled the complete publisher HTML. Section IV describes Paillier additive homomorphic encryption with binary modular exponentiation, symmetric searchable encryption, Bloom-filter indexes, and Hyperledger Fabric access control. The reported implementation uses Fabric 2.2, CouchDB, Go chaincode, organization-unit attributes, and private data collections. Algorithm 1 sets indefinite retention (`blockToLive = 0`). Section IV.C explicitly describes decrypting retrieved medical records before sharing them with an authorized requester. The extracted boundary therefore distinguishes ciphertext aggregation from subsequent plaintext release.

Section V reports an Ubuntu 20.04 / Intel Core i7-11800H setup, encryption-key lengths of 512–4,096 bits, and a selected 2,048-bit key for file-size experiments. Search experiments use 10,000–50,000 records of 200 bytes each. Figures 2–7 report encryption, search, and storage measurements. The authors report a mean 34% encryption/decryption time reduction against their comparator. No independent reproduction is performed here, and a generic claim of improved Paillier complexity is not inferred from that measurement.

The security discussion in V.A assumes IND-CPA encryption but does not give a reduction for the complete composed system. Its ciphertext-collision argument does not establish indistinguishability. Hash irreversibility is not a proof of search-pattern confidentiality. The article's own Section VII acknowledges Bloom-filter false positives, resource costs, and operation limits. Membership controls and the reported measurements do not prove protection against authorized-recipient misuse, downstream deletion, or correctness of outsourced computation. No public project repository was identified in the inspected primary text. Evidence supports G2, G3 (key custody/release), G4 (computation integrity), G5, and G7 (output inference).

## Qu, Yang, Chen, and Sun: consent-aware medical records

Primary publication: [A consent-aware electronic medical records sharing method based on blockchain](https://doi.org/10.1016/j.csi.2024.103902), *Computer Standards & Interfaces* 92, 103902 (March 2025). Original observation: S04, rank 7, page 1. Decision: eligible application study, consent group. Complete publisher HTML was inspected through institutional access.

Sections 3.1–3.3 and Table 3 specify a patient-mediated transfer between the institution holding the record and the institution requesting it. The patient retrieves an encrypted IPFS object, decrypts it, encrypts it again with a temporary symmetric key, and releases the new content identifier and key to the recipient. Ethereum contracts record the business stages. Traceable ring signatures authenticate recorded exchanges and support signer tracing. Registration and assignment of identity are explicitly outside the method's detailed scope.

Sections 4.1–4.3 report Solidity contracts tested with Ganache and Remix, transaction-load tests from 0 to 200 pending requests, 3–20 users, and records of 400–1,000 bytes. Ring-signature experiments vary ring size from 20 to 100. Section 5.2 gives signature lemmas and a tag-linkability argument in the random-oracle model. These are distinct from the qualitative system security discussion in Section 5.1. No public project repository was identified in the inspected text.

The mechanism implements an authorization and key-release workflow. It does not establish downstream deletion, prevention of recipient copying, truthful clinical inputs, or general legal compliance. Patient mediation does not by itself terminate the originating institution's legal duties. The article's PoW and majority-attack discussion is not adopted as evidence about contemporary Ethereum deployment. Evidence supports G1, G2, G3, G5, G6, and G8 (input provenance).

## Rao and Selvan: genomic consent

Primary publication: [Empowering Genomic Data Sharing in Healthcare: A Blockchain-Driven Decentralized Consent Model](https://doi.org/10.1109/I-SMAC61858.2024.10714793), I-SMAC 2024, conference 3–5 October 2024, added to IEEE Xplore 23 October 2024. Original observation: S04, rank 18, page 2. Decision: eligible application study, consent group. Method and evaluation were inspected in the complete publisher HTML.

Sections III–IV specify a patient, requester, attribute authority, encrypted consent record, SHA-256 token, RSA recipient encryption, smart-contract authorization, and encrypted off-chain genomic data. The attribute authority generates user keys. Section V reports a proof of concept using Solidity, Ganache, Remix, JPBC, and a CP-ABE toolkit on synthetic datasets of 10, 50, 100, 500, and 1,000 records. Tables 2–5 cover encryption/decryption time, key generation, and storage. A named deployed consortium platform is not established by this Ethereum development-tool setup. No public project repository was identified.

The access policy and current consent state govern future requests. The text does not specify a key/ciphertext update protocol that invalidates previously released material after revocation. The ABE formulas and qualitative discussion do not provide a security reduction for the complete system. Trust/autonomy and legal-compliance claims are not established by the reported cryptographic timing measurements. Evidence supports G1, G2, G3, G6, and G8.

## Scaramuzza et al.: zero-knowledge consent

Primary publication: [Zero-Knowledge Consent: Auditable and Private Data Permission Management via Blockchain](https://doi.org/10.1109/SANER-C67878.2026.00011), SANER-C 2026, conference 17–20 March 2026, added to IEEE Xplore 6 May 2026. Original observation: S04, rank 22, page 3. Decision: eligible application study, consent group. Sections IV–IX were inspected in complete publisher HTML.

Ethereum contracts register participants and encrypted permission requests, verify proofs, and record approvals and revocation. The Circom/snarkjs circuit proves knowledge of a secret whose Pedersen hash matches a public commitment. The ledger records permission status. A local React interface generates proofs. A one-off setup produces hard-coded proving and verification keys. Metadata encryption uses RSA-512.

Sections IV.E and VII report black-box requirement tests and single-machine benchmarks using Ganache/Truffle on an i7-8700 with 16 GB RAM. Five measured cryptographic/encoding operations were repeated 10 times. Proof and public-signal generation account for 98.8% of measured computation, with nearly 10 seconds reported in VIII.C. The authors report 15 of 17 functional requirements satisfied. Age verification and formal notification remain unresolved. No public project repository was identified in the inspected article links.

The paper explicitly recognizes that RSA-512 compromises metadata confidentiality, setup-secret retention enables proof forgery, approval exposes participant links, and off-chain erasure remains an act of trust. Its absence-of-consent argument depends on complete ledger records and the assumed account/permission linkage. The circuit proves a commitment relation, not factual data use, complete audit capture, or regulatory compliance. Evidence supports G1, G2, G3, G5, G6, and G8.

## Ferreira et al.: MCP/FHIR consent

Primary publication: [Blockchain Integration for Trust and Consent Management in MCP-Enabled FHIR Systems](https://doi.org/10.1109/ICDLT66400.2025.11466653), ICDLT 2025, conference 5–7 November 2025, added to IEEE Xplore 16 April 2026. Original observation: S04, rank 25, page 3. Decision: eligible application study, consent group. Sections IV–VI were inspected in complete publisher HTML.

The method combines a Model Context Protocol gateway, FHIR endpoints, DID/VC identities, a ConsentRegistry, and a ProvenanceLedger. The gateway checks purpose, scope, time, current consent, and credential status. It hashes returned bundles and records query manifests. Issuer allowlists and periodic revocation-list polling govern credential trust and propagation. LLM summaries carry an audit handle. The text presents permissioned Fabric or an EVM L2 as alternatives rather than identifying one measured deployment consistently. Zero-knowledge attestations are described as conditional extensions.

Section V.D reports 300 randomized requests, 75 per arm, with OAuth2/UMA, signed logs, TEE, and blockchain/VC comparators. It reports a median 870 ms and revocation propagation of 1.8 seconds. Table 3 is explicitly captioned "Illustrative results". Sections IV.B/IV.F and V.D differ on single versus multiple clinical domains and synthetic versus institution-origin records. These inconsistencies limit what can be inferred about the evaluation. No reproducible experiment repository was identified in the inspected text.

Hashes bind logged data representations. They do not prove correctness of a generated clinical summary or completeness of omitted inputs. Issuer trust, gateway checks, cache invalidation, and truthful source data remain conditions. The survey does not repeat patient-outcome or regulatory-compliance claims as established results. Evidence supports G1, G2, G5, G6, and G8.

## Ayala-Tipan et al.: personal-data consent records

Primary publication: [Data Consent Management: A Blockchain Solution for User Empowerment and Trust](https://doi.org/10.1109/ICEDEG61611.2024.10702050), ICEDEG 2024, conference 24–26 June 2024, added to IEEE Xplore 8 October 2024. Original observation: S04, rank 17, page 2. Decision: eligible application study, consent group. Sections V–VIII were inspected in complete publisher HTML.

The system stores consent, recipient, and personal-data records in hash-linked blocks with a separate company-specific hash chain. The article describes encryption and release of decryption keys to approved companies. Its reported proof of concept uses React, Node.js, and MongoDB. The public [BlockChainConsent repository](https://github.com/BorisCaiza/BlockChainConsent) was verified and contains the front end, back end, and synthetic-data generator. No distributed consensus deployment is established by this implementation evidence.

Section VIII reports eight synthetic block-count scenarios, 10 runs per scenario, and mean create/edit/delete times of 3.3108/2.4051/2.5382 seconds. These are local operation measurements rather than proof of distributed fault tolerance. The qualitative mapping to Ecuador's LOPDP and GDPR is not a legal compliance assessment. Withdrawal appends a new consent state. It does not erase prior blocks or invalidate data already decrypted by recipients. The reported zero failure rate does not establish resilience to node or network faults that were not injected. Evidence supports G1, G2, G3, G5, and G6.

## Liu et al.: SS-DID

Primary publication: [SS-DID: A Secure and Scalable Web3 Decentralized Identity Utilizing Multilayer Sharding Blockchain](https://doi.org/10.1109/JIOT.2024.3380068), *IEEE Internet of Things Journal* 11(15), 25694–25705. First published 21 March 2024, issue 1 August 2024. Original observation: S07, rank 6, page 1. Decision: eligible application study, identity group. Sections III–VI were inspected in complete publisher HTML.

Regular shards process signed DID registration, updates, deactivation, and credential events. Field-leader shards authorize cross-field verification. A main chain anchors management records. Aggregate BFT certificates and Merkle proofs connect credential checks across shards. Hospital, pharmacy, and insurer examples distinguish holder, issuer, and verifier roles. Deactivation records a new state and ends further DID updates. It does not remove prior credential-use records.

The security argument assumes unforgeable signatures, authenticated channels, partial synchrony, and a Byzantine fraction below one third within committees. Its stated goals are DID-message unforgeability and system liveness. These do not establish selective disclosure or unlinkability. Credential-use transactions record DIDs, credential hashes, issuer and verifier identifiers, permitting linkage within the recorded workflow.

Section VI presents simulations with 100 Mb/s bandwidth, 50 ms communication delay, 1 kB requests, batches of 2,000, and 30–60 nodes per shard. Comparators are PBFT and HotStuff variants. The best reported overall throughput is 90,000 requests/s for five fields, 20 shards per field, and 30 nodes per shard. This is a simulation result, not deployed throughput. No public project repository was identified in the inspected primary text. Evidence supports G2, G5, G6, and G8.

## Kadar et al.: native record resolved, outside application scope

Primary publication: [Blockchain and Machine Learning Approaches to Enhancing Data Privacy and Securing Distributed Systems](https://doi.org/10.1109/INDISCON66021.2025.11251973), INDISCON 2025. The native IEEE authors are Mohamad Abdul Kadar, Suthari Yugandhar Reddy, Prakruti Parmar, Jobanpreet Kaur, Vishvanatha Raju, and Siva Koteswara Rao Katta. Conference 21–23 August 2025, added 2 December 2025. Original observation: S01, rank 8, page 1. Decision: exclude from application collection.

Sections III–IV were inspected in complete publisher HTML. The evaluated workflow detects intrusions/anomalies in synthetic transaction, access, and network logs. Healthcare and finance are motivating examples. No specific personal-data sharing, consent, or holder/issuer/verifier application is defined. Exclusion follows application scope, not venue prestige or perceived paper quality. The earlier, homonymous 2023 source is not used to assess or deduplicate this native 2025 record.

## Kumar et al.: healthcare review, outside the application denominator

Primary publication: [Enhancing Healthcare with Blockchain: Innovations in Data Privacy, Security, and Interoperability](https://doi.org/10.1109/ICDT63985.2025.10986335), ICDT 2025, conference 7–8 March 2025, added to IEEE Xplore 13 May 2025. Authors: Bhupendra Kumar, Vishal Garg, Kahksha Ahmed, Puneet Garg, Shweta Choudhary, and Pashupati Baniya. Original observation: S01 rank 4. Decision: secondary review, not an application addition.

The seven-page publisher PDF was downloaded under institutional access and inspected. Sections II–III discuss blockchain concepts and parallel healthcare. Section IV and Table II summarize applications from other papers. Sections I and V describe the paper's review purpose. Statements about Truffle/Ganache in the background do not identify an original evaluated sharing protocol. No application extraction is added. The inspected PDF is retained in the local download directory, not redistributed in the survey dataset.

## Deepthika et al.: permission checks with predicted preferences

Primary publication: [Blockchain-Integrated Deep Learning for Secure Health Data Sharing and Consent Management](https://doi.org/10.1109/ICoICI62503.2024.10696868), ICoICI 2024, 101–106. Conference 28–30 August 2024, added to IEEE Xplore 4 October 2024. Authors: K. Deepthika, G. Shobana, Kumbam Venkat Reddy, Srimathi S, Binod Kumar, and Shrikant Upadhyay. Original observation: S04 rank 9. Decision: eligible descriptive consent/permission proposal.

Complete publisher HTML Sections II–III specify a Fabric transaction sequence that authenticates a requester and checks permissions before submission. An LSTM is proposed to predict changing preferences and adapt access rights. Descriptive workflow eligibility is applied consistently with the other conceptual studies. This decision does not endorse the proposed rule for inferring permission.

The experiments use CICIDS-2017 and NSL-KDD intrusion datasets. Section III and Table II report 750 transactions/s, 92% prediction accuracy, and 88% consent-management accuracy, but do not establish how explicit patient consent is represented or how consent labels and ground truth are obtained from those datasets. Hashing is described as privacy preservation without a confidentiality protocol. No public experiment repository was identified. Predicted preferences are not evidence of freely given informed consent, and classification accuracy does not validate a healthcare consent workflow. Evidence supports G1, G2, and G8.

## Gupta et al.: certificate permission proposal

Primary publication: [Decentralized and Permission-Aware Blockchain for Certificate Security: An Exploratory Analysis](https://doi.org/10.1109/ICSCSS60660.2024.10625663), ICSCSS 2024, 558–562. Conference 10–12 July 2024, added to IEEE Xplore 20 August 2024. Authors: Neha Gupta, Shweta Negi, Khyaty Rawat, and Megha Rawat. Original observation: S04 rank 29. Decision: eligible descriptive permission/credential proposal, accounted under its permission-query family.

Complete publisher HTML Sections III–IV describe stakeholder interviews/surveys and a proposed permissioned Fabric certificate service. Authorized issuers create certificates and smart contracts govern issuance, checking, and revocation. Hashes and digital signatures are the stated integrity controls. This is an identifiable proposed application, satisfying the descriptive eligibility rule independently of evaluation quality.

Section IV's comparison and certificate-forgery figure do not describe a reproducible attack experiment establishing the claimed reduction. The examined text does not establish a deployed Fabric topology, a public implementation repository, selective disclosure, or recipient confidentiality. Stakeholder perceptions and comparison claims are distinguished from measured protocol security. Evidence supports G1, G2, G6, and G8.

## Hemlata et al.: DualCare

Primary publication: [DualCare: A Blockchain Framework for Secure Medical Data Sharing with Dual Consent](https://doi.org/10.1109/ICBC67748.2026.11575533), ICBC 2026. Conference 1–5 June 2026, added to IEEE Xplore 1 July 2026. Authors: Kumari Hemlata, Sanjana Saxena, Divyansh Barodiya, Raman, Sujata Pal, and Shantanu Pal. Original observation: S04 rank 30. Decision: eligible consent application.

Complete publisher HTML Sections III–V specify two Fabric networks, an event-driven Node.js relay, RBAC middleware, AES-256 encrypted records in MinIO, and RSA-2048 wrapping of released record keys. Hospital and patient approvals must both be recorded before middleware releases a key. Revocation propagates through the relay and deletes the stored wrapped key. Algorithms 1–2 describe authorization and key handling.

Two Fabric test networks with Raft ordering were evaluated over 20 workflows. Section V and Tables II–III report a mean complete-workflow latency of 12.824 s, approximately 2.044 s for writes and 2.053 s for relay propagation. These are controlled test-network results. A public implementation repository was not identified in the inspected article.

The relay carries consent state and the middleware holds record keys. Deleting a wrapped key from middleware does not invalidate the plaintext AES key already recovered by a recipient. Expiry is an access rule rather than a cryptographic expiry property of an exported AES key. Hash comparison binds returned bytes to recorded hashes, not clinical truth. The article's claim that HIPAA/GDPR universally require dual organizational/patient consent is not adopted. Evidence supports G1, G2, G3, G5, G6, and G8.

## Seidi and Abdellaoui: healthcare SSI and role permissions

Primary publication: [Securing and Ensuring the Confidentiality of Medical Data in the Era of Decentralized Technologies: A Blockchain and Self-Sovereign Identity-Based Approach](https://doi.org/10.1007/s10922-025-09960-x), *Journal of Network and Systems Management* 33, 81. Published 4 July 2025. Original observation: S07 rank 8. Decision: eligible identity application. Complete publisher HTML Sections 3–7 was accessed through USP/CAPES.

Hospitals/doctors issue signed credentials, patients hold credentials and presentations, and pharmacies/insurers verify them. Ethereum stores DID documents and record identifiers, IPFS stores records, and an administrator assigns roles and grants/revokes role permissions. The DApp uses Veramo for credential/presentation signing and verification. Section 4 reports Sepolia deployment. Sections 3.2.4 and 5, Tables 2 and 4–5, report gas, timing, CPU/memory, and verification experiments with 50 repetitions and 10 parallel sessions.

PII hashing does not establish confidentiality of low-entropy attributes. A holder-signed presentation containing an issuer-signed credential does not by itself establish cryptographic selective disclosure. The descriptive DID format and compatibility claims were not independently tested against a resolver. Administrator authority, trusted issuer assertions, and off-chain storage remain dependencies. Section 7 explicitly leaves interoperability and jurisdictional compliance unvalidated. No public project repository or reproducible experiment package was identified in the examined article. Evidence supports G1, G2, G5, G6, and G8.

## Lu et al.: controlled editing of educational records

Primary publication: [Redactable blockchain with anonymity and multi-permission for instructional management](https://doi.org/10.1016/j.bcra.2024.100247), *Blockchain: Research and Applications* 6(1), 100247, March 2025. Authors: Xiuhua Lu, Jing Liu, Fengyin Li, Jiazheng Zou, and Yuhao Hou. Original observation: S04 rank 27. Decision: eligible permission application. Complete publisher HTML Sections 3–5 was inspected.

Students query scores and submit anonymous disputes. Teachers/counselors enter records. A review team comprising counselor, teaching inspector, and teaching secretary must cooperate to edit a disputed record. Linkable-claimable ring signatures protect reporter identity within the specified relation and allow voluntary identity claiming. A multi-permission chameleon hash uses master/ephemeral trapdoors plus a counselor signature to constrain modification.

Sections 4.3–4.4 state partial trust in the review roles and present correctness, CDH/DCDH-based collision-resistance, and claimability arguments. These are source-reported conditional results, not an independent proof audit. Section 5 reports Python/Pypbc/ECDSA/Py-eth/Py-tester experiments on an Ubuntu Xeon server, averages over 100 executions, and EVM simulation with 10,240–204,800-byte messages. No public project repository was identified in the examined text.

The scheme controls score editing and report attribution. It does not establish confidentiality of all student records, truth of a corrected score, deletion of prior external copies, or general GDPR compliance. Editing authorization is distinct from data-subject consent to secondary processing. Evidence supports G1, G2, G3, G6, and G8.

## Gupta, Kumar, and Gupta: federated lung-disease detection

Primary publication: [A blockchain-empowered federated learning-based framework for data privacy in lung disease detection system](https://doi.org/10.1016/j.chb.2024.108302), *Computers in Human Behavior* 158, 108302 (2024). Authors: Mansi Gupta, Mohit Kumar, and Yash Gupta. Original observation: S01 rank 10. Decision: eligible privacy application. Complete publisher HTML Sections 4–5 was inspected through institutional access.

Sections 4.1–4.2 and Algorithms 1–3 describe local DenseNet training at hospitals, hierarchical aggregation through federated routers/backend servers, signed user/model references, IPFS storage, and contract record checks. The consortium/PoA deployment is described, rather than demonstrated by a reproducible distributed benchmark. Table 4 reports two clients and 15 rounds. Tables 3–5 and Section 5.2 report image-classification experiments, with inconsistent sample totals and image modality descriptions. No sample total is inferred from the conflicting prose. No public project repository was identified.

Section 5.3 treats SHA-256 as encryption, signatures as user confidentiality, and hash-chain integrity as poisoning resistance. These inferences are not adopted. The proposed workflow is eligible independently of the strength of these claims. Federated model sharing does not establish confidentiality of exchanged updates, and authenticating a model does not establish that its training data or gradients are benign. The study supports G2, G4, G7, and G8 through these boundaries.

## Joseph: financial comparison, native version resolved

Original observation: S01 rank 2, [SSRN 4949837](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4949837). Its native header was accessed on 1 October 2026 after automatic site verification. It identifies Sunday Joseph, explicitly links the *Journal of Engineering Research and Reports* 26(9) article and DOI [10.9734/jerr/2024/v26i91271](https://doi.org/10.9734/jerr/2024/v26i91271), states 21 pages, a posting date of 11 October 2024, and a writing date of 7 September 2024. This resolves the journal-version association that prevented the earlier decision.

The journal primary text was already inspected in the preceding assessment recorded in `update-assessment-2026-10-01.csv` (Section 3 and Sections 4.1–4.3). It compares existing financial platforms and transaction-sensitivity scenarios and reports Ethereum-testnet comparisons. It does not specify an identifiable application-level personal-data sharing, permission, or identity workflow under the adopted criterion. Decision: exclude for application scope. This does not deny that the paper discusses privacy technologies or financial transactions. The SSRN download did not complete, and the publisher currently raises a certificate warning, which was not bypassed. The decision uses the previously inspected published text plus the now-verified native version linkage.

## Abdullah et al.: remaining access-dependent assessment

Original observation: S01 rank 3. [Blockchain Adoption in Education with Enhancing Data Privacy](https://doi.org/10.1007/978-3-031-60221-4_42), Khadeejah Abdullah, Kassem Saleh, and Paul Manuel, first online 13 May 2024, pages 445–455. Institutional Springer access is working for other sources, but this chapter still displays subscription preview without a Download PDF link. The abstract mentions both a review and an original simulation. It cannot establish which workflow was specified. Decision remains pending primary full text, not excluded.
