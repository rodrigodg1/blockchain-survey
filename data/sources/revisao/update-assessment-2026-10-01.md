# Evidence records for included publications

Each included row below links the actual examined source. The CSV also retains the observed native result URL, which may have been inaccessible or less precise.

### updateHussain2025ZeroTrust

**Source/version:** [Ensuring Zero Trust IoT Data Privacy: Differential Privacy in Blockchain Using Federated Learning](https://ndownloader.figshare.com/files/65056158); Accepted author manuscript carrying publisher DOI; final issue 71(1), February 2025. DOI: [10.1109/tce.2024.3444824](https://doi.org/10.1109/tce.2024.3444824).

**Locator:** III.A (LDP statement); IV and Algorithm 1 (sharing workflow); V (implementation and evaluation), author manuscript pp.5–10.

**Evaluation:** Reported Python FL/noise simulation and 70 trading rounds; transaction and accuracy comparisons.

**Boundary:** Privacy unit, operational noise calibration and composition accounting are insufficiently specified; the stated LDP argument does not establish privacy of this training procedure; accuracy and cost-derived latency/throughput are not privacy guarantees.

### updateBarnes2025DemonstratedConsent

**Source/version:** [Enabling Demonstrated Consent for Biobanking with Blockchain and Generative AI](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12005476/fullTextXML); Published article; online 2024-11-05; issue 25(4), 2025. DOI: [10.1080/15265161.2024.2416117](https://doi.org/10.1080/15265161.2024.2416117).

**Locator:** III Demonstrated Consent; IV Implementing Demonstrated Consent with Blockchain and Generative AI; VI Limitations and Future Directions.

**Evaluation:** Conceptual mechanism and ethical analysis; explicitly no functioning prototype.

**Boundary:** No implemented transfer gate, donor-comprehension test, security evaluation or measured withdrawal propagation; proposed NFT/smart-contract workflow does not itself constrain physical sample use or downstream copies.

### updateRohini2024SmartConsent

**Source/version:** [Smart Patient Consent Management Model for Health Information Exchange Based on Blockchain Technology](https://thescipub.com/pdf/jcssp.2024.730.741.pdf); Publisher PDF, Journal of Computer Science 20(7), 730–741; 2024-07-01. DOI: [10.3844/jcssp.2024.730.741](https://doi.org/10.3844/jcssp.2024.730.741).

**Locator:** Materials and Methods pp.734–737; Implementation/Prototype System p.737; Results and Discussion pp.737–739.

**Evaluation:** Four-Linux-PC Fabric prototype; functional consent/access cases and reported latency/cost comparisons.

**Boundary:** Clinical deployment and downstream use are not established; Ethereum-style gas accounting in a Fabric comparison lacks an identified mapping, so quantitative cost advantages are not imported.

### updateBonotis2025CONSENT

**Source/version:** [Enabling Dynamic Consent Through AI and Blockchain: The CONSENT Platform](https://journals.sagepub.com/doi/10.3233/SHTI251556); Published SHTI 332 contribution, 330–334, 2025; corrected article DOI. DOI: [10.3233/shti251556](https://doi.org/10.3233/shti251556).

**Locator:** 2.1–2.3 (architecture); 3 (planned results/evaluation); 4 (discussion).

**Evaluation:** Architecture proposal; evaluation scenarios and metrics are planned, not completed results.

**Boundary:** No demonstrated prototype, measured withdrawal propagation, user comprehension, security or legal-compliance assessment; AI recommendations do not establish valid consent.

### updateTomaz2025PrivacHer

**Source/version:** [Trust Through Transparency: Blockchain for Consent and Accountability in Femtech Applications](https://www.researchgate.net/publication/397291306_Trust_Through_Transparency_Blockchain_for_Consent_and_Accountability_in_FemTech_Applications); Author-uploaded published GoodIT 2025 paper, pp.33–40; conference 2025-09-03. DOI: [10.1145/3748699.3749771](https://doi.org/10.1145/3748699.3749771).

**Locator:** Published full-text header (GoodIT 2025 DOI); 3.2–3.3 (services/Fabric); 4.1–4.2 (tests).

**Evaluation:** Functional registration/consent/retrieval and end-to-end workflow tests; Locust load tests of latency and throughput.

**Boundary:** API access checks and logs do not establish control of recipients after disclosure or GDPR compliance; published source supports functional/load evidence, not a regulator-endorsed deployment.

### updateOke2025FHIRConsent

**Source/version:** [Blockchain-Enabled Consent Management in FHIR-Compliant Oncology Platforms](https://www.researchgate.net/publication/392500406_Blockchain-Enabled_Consent_Management_in_FHIR-Compliant_Oncology_Platforms); TechRxiv preprint v1, 2025-06-06; native result v2 (2025-06-18) verified as same title/authors but not accessible. DOI: [10.36227/techrxiv.174918103.37396756/v1](https://doi.org/10.36227/techrxiv.174918103.37396756/v1).

**Locator:** Methodology: System Architecture (FHIR–Blockchain Bridge); Consent Workflow steps 1–3; Results and Discussion.

**Evaluation:** Conceptual architecture and discussion using prior implementations; no evaluation of this proposed system.

**Boundary:** Adapter consistency, failure handling and current-state enforcement are not measured; no recall of previously disclosed data; extraction applies to v1 only, not unexamined v2.

### updateMiao2026PermissionSupervision

**Source/version:** [A Verifiable and Redactable Blockchain with Lightweight Storage and Permission Supervision](https://mdpi-res.com/d_attachment/information/information-17-00176/article_deploy/information-17-00176.pdf); Publisher PDF, Information 17(2), 176, 2026-02-09. DOI: [10.3390/info17020176](https://doi.org/10.3390/info17020176).

**Locator:** 3.1–3.3 (roles/threat model); 4.1–4.2 (construction); 5–6 (analysis/evaluation).

**Evaluation:** Formal construction/security arguments and primitive/audit performance analysis.

**Boundary:** Fully trusted CA remains; controlled on-chain redaction does not establish deletion of off-chain copies, patient consent or full compliance; primitive benchmarks are not an end-to-end sharing deployment.

### updateCh2026ConsentOffloading

**Source/version:** [A consent-based medical data sharing and edge offloading scheme based on blockchain and deep reinforcement learning](https://link.springer.com/article/10.1007/s10791-026-10392-7); Published publisher HTML, Discover Computing 29, 533, 2026-08-13. DOI: [10.1007/s10791-026-10392-7](https://doi.org/10.1007/s10791-026-10392-7).

**Locator:** 3 (system model); 4–5 (offloading and sharing); 6 (performance evaluation).

**Evaluation:** Single Windows/WSL host; Besu networks of 4/6/8/10 nodes; Caliper transaction tests and simulated offloading.

**Boundary:** Edge processing receives plaintext and recipients obtain decryption keys; approval/ledger state does not recall disclosed data; private-network/honest-miner assumptions and local measurements limit deployment claims.

### updateDauden2025RTBConsent

**Source/version:** [Blockchain-Enhanced User Consent for GDPR-Compliant Real-Time Bidding](https://crises-deim.urv.cat/uploads/publications/1282.pdf); Author manuscript linked by CRISES to DBSec 2025; publisher chapter online 2025-06-24. DOI: [10.1007/978-3-031-96590-6_8](https://doi.org/10.1007/978-3-031-96590-6_8).

**Locator:** 3.2–3.5 (architecture and three phases); 4.1–4.4 (propositions); author manuscript pp.8–16.

**Evaluation:** Architectural proposal with prose propositions/claims; no reported prototype benchmark.

**Boundary:** Compliance claims depend on participating websites, data repositories and advertising actors; no measured revocation propagation, recall of recipients copies, or independent assessment of valid consent.

### updateAlSabahi2026AuthorshipConsent

**Source/version:** [Self-sovereign identity for verifiable authorship consent and privacy-preserving conflict-of-interest screening in academic publishing: a permissioned blockchain registry approach](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2025.1730645/full); Published 2026-04-01; publisher volume 8 and DOI suffix 2025 do not determine publication year. DOI: [10.3389/fbloc.2025.1730645](https://doi.org/10.3389/fbloc.2025.1730645).

**Locator:** 4.4–4.6 (workflow/status/circuit); 4.8–4.10 (indicative cost and pilot); 5.1 (formative survey).

**Evaluation:** Specified relations, circuit/chaincode sketches and formative stakeholder questionnaire; indicative Groth16 costs are extrapolated.

**Boundary:** No implemented registry/ZK benchmark or demonstrated effectiveness; possession of declared affiliation evidence does not establish completeness/truth of all affiliations; limited predicates do not prove full conflict-of-interest absence.

### updateNaghmouchi2026ClinConNet

**Source/version:** [ClinConNet: A Blockchain-Based Dynamic Consent Management Platform for Clinical Research](https://arxiv.org/html/2602.02610); arXiv:2602.02610v1, 2026-02-02; explicitly a preprint. DOI: [10.48550/arXiv.2602.02610](https://doi.org/10.48550/arXiv.2602.02610).

**Locator:** 4.3 (trust assumptions); 5.1–5.3 (workflow); 6 (privacy analysis scope); 7.1–7.5 (testbed/metrics); Data availability.

**Evaluation:** Single-host two-peer/one-orderer Fabric PoC; browser cryptographic-operation and Caliper tests; lifecycle timing sums component medians.

**Boundary:** Honest-but-curious portal/cloud and Tor assumptions; disclosed clinical data excluded from privacy analysis; component-time sum omits network/human delay; proof revocation or portal-mapping deletion does not ensure erasure of researchers data.

### updateObodo2025MultiProviderConsent

**Source/version:** [Conceptualising Blockchain-Based Consent Management in Multi-Provider Healthcare Environment](https://ijsrmt.com/index.php/ijsrmt/article/download/817/255/4908); Publisher PDF, IJSRMT 4(9), 116–121, published 2025-09-20. DOI: [10.38124/ijsrmt.v4i9.817](https://doi.org/10.38124/ijsrmt.v4i9.817).

**Locator:** III Theoretical Framework/Conceptual Model pp.117–118; IV Benefits, Challenges, and Considerations pp.118–119.

**Evaluation:** Conceptual model and discussion; no prototype or measured evaluation.

**Boundary:** Immediate cross-provider propagation and savings are proposed or attributed to other works, not measured here; identity method, keys and enforcement implementation remain unspecified.

### updateGupta2026ScalableConsent

**Source/version:** [Scalable Blockchain-Based Healthcare Consent Management with Automated Compliance Verification](https://convecs.inria.fr/doc/publications/Gupta-Lang-Ozeer-Salaun-26.pdf); Author manuscript linked by Inria and HAL hal-05730325; COMPSAC 2026 publication 2026-07-07. DOI: [10.1109/compsac69091.2026.00125](https://doi.org/10.1109/compsac69091.2026.00125).

**Locator:** IV (consent/synchronization); V (proof inputs and checks); VI.A–C (implementation/workload/metrics), author manuscript pp.4–9.

**Evaluation:** Single local 8-core/8-GB host; synthetic consent populations of 500000–10000000 patients; query comparisons and reported proof costs.

**Boundary:** Chosen predicates on supplied inputs do not certify all actual processing or legal compliance; raw data are released to processors; local synthetic results and cross-paper comparisons do not establish production performance or superiority over encrypted computation.

### updateRen2025AIoTIdentity

**Source/version:** [Blockchain-Based Self-Sovereign Identity Management Mechanism in AIoT Environments](https://mdpi-res.com/d_attachment/electronics/electronics-14-03954/article_deploy/electronics-14-03954.pdf); Publisher PDF, Electronics 14(19), 3954, 2025-10-08. DOI: [10.3390/electronics14193954](https://doi.org/10.3390/electronics14193954).

**Locator:** 3.1–3.4 (mechanism); 4 (security arguments); 5.1–5.5 (synthetic experiment).

**Evaluation:** Mathematical arguments and synthetic 10000-user/20-attribute experiments on a local Ubuntu host.

**Boundary:** Synthetic credential/permission tests are not deployed sharing or downstream use control; correlation-attack metrics are not equivalent to DP guarantees; trust in KGC and correct context evaluation remains.

### updateZeydan2024ABSIdentity

**Source/version:** [Blockchain-based self-sovereign identity solution for aerial base station integrated networks](https://zenodo.org/records/12781373/files/Blockchain-based%20self-sovereign%20identity%20solution%20for%20aerial%20base%20station%20integrated%20networks.pdf?download=1); Author manuscript deposited by CTTC researchers; final Vehicular Communications 47, 100759, June 2024. DOI: [10.1016/j.vehcom.2024.100759](https://doi.org/10.1016/j.vehcom.2024.100759).

**Locator:** 2–3 (architecture/ABS interactions); 4.1–4.3 (testbed/metrics); author manuscript pp.5–17.

**Evaluation:** Two OpenStack VMs; four container issuer nodes; credential/DIDComm operations for 50000/75000/100000 requests.

**Boundary:** Credential-operation tests do not establish real multi-operator radio deployment, inference privacy or control after credential disclosure; underlying issuers and operator authentication infrastructure remain trusted.

### updateRamirez2025IOTAIdentity

**Source/version:** [Decentralized Identity Management for Internet of Things (IoT) Devices Using IOTA Blockchain Technology](https://rua.ua.es/server/api/core/bitstreams/2840e453-d856-461e-8678-f6803595b60d/content); Published author/institutional full text, Future Internet 17(1), 49, 2025-01-20. DOI: [10.3390/fi17010049](https://doi.org/10.3390/fi17010049).

**Locator:** 3.1–3.2 (materials/workflow); 4.1 (DIDComm limitation); 4.2–4.3 (channel operations and performance).

**Evaluation:** Raspberry Pi 4 (4 GB) prototype; identity/message workflows and reported resource/latency comparisons.

**Boundary:** DIDComm is explicitly not integrated and interactions are simulated; credential/channel tests do not establish recall of previous data or deployed large-scale security; libraries describe the paper version, not current support.
