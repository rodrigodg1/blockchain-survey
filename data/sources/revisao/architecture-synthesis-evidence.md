# Analytical comparison and evidence boundaries

Historical revision date: 1 October 2026. This note records the initial analytical revision at the 106-application stage (98 historical records and eight initial update inclusions), before later assessment and reorganization. It does not state the current collection size or current research questions. Current counts are in [counts.json](../../counts.json); the current three-RQ comparison is documented in [synthesis-codebook.md](synthesis-codebook.md).

## Recorded analytical changes

The revision related decision authority, permission, enforcement points, trust boundaries, and evidence. It separated permission to invoke a service, computation on protected inputs, and release of decrypted results. Requirements were derived from qualitative comparisons rather than a new uniform extraction or a validated taxonomy. Study identities and existing results tables were preserved; no studies were removed to favor an application sector, and no new classification was assigned to the 106 records at that stage.

The initial requirement table distinguished five boundaries: identity/authority, permission/release, confidentiality/correctness, audit evidence/disclosure, and withdrawal/credential status. Each related existing sources to a requirement and assessment question. Proposed evaluations included valid credentials with withdrawn permission, unauthorized release, and an incorrect result under valid permission. These were proposed tests, not added experimental results. The current eight criteria and their derivations are documented separately in [synthesis-evidence-method.md](synthesis-evidence-method.md).

## Sources and examined material

The bibliographic addition at this stage was contextual:

- Garcia, Ramachandran, Rothenberg, Krishnamachari, and Ueyama. *A Survey of Privacy-Preserving Mechanisms on Quality of Experience in Next-Generation Networks*. Computer Networks 275 (2026), 111899. DOI: [10.1016/j.comnet.2025.111899](https://doi.org/10.1016/j.comnet.2025.111899), key `GarciaComNet2026`. Metadata were checked through an official ScienceDirect search record; direct access returned 403. The content comparison used an examined local manuscript copy, specifically Contributions, Architectural Approaches, and User-Centric Privacy and Trust. The cited year is 2026; the year in the DOI does not replace the publication year. The comparison recognizes that this review already discusses governance, identity, and credentials as future directions.

The public-evaluation distinction uses the existing reference `homenc`: Craig Gentry, *A Fully Homomorphic Encryption Scheme*, Stanford, 2009. Section 2.1, printed page 27 (PDF page 37), defines Evaluate with a public key, circuit, and ciphertexts. Section 1.8, printed page 21 (PDF page 31), distinguishes server evaluation from result recovery by the secret-key holder. The [primary PDF](https://crypto.stanford.edu/craig/craig-thesis.pdf) was accessed over HTTP after the web reader failed. This theoretical source was not added to the application collection.

| Initial comparison boundary | Previously analyzed sources | Preserved limit |
|---|---|---|
| Identity/authority | Zeydan; Phuyal's conceptual design | Authentication does not establish permission or inference privacy. |
| Permission/release | Can; SecureConsent; Gao's PRE/ABE delegation | A record or token does not establish control of every subsequent use. |
| Confidentiality/correctness | Smart-grid homomorphic aggregation; Gentry; Zerocash | Checked relations and hidden data have their own definitions and assumptions. |
| Audit evidence/disclosure | Can; BADIMAC; AnonCreds | An intact log does not establish event completeness; selective disclosure does not eliminate all metadata. |
| Withdrawal/status | SecureConsent; Phuyal; Bitstring Status List | Future access denial, credential revocation, and removal of copies are distinct outcomes. |

The revision did not establish primacy or absence of overlap with other surveys. Nguyen, Phuyal, Mazzocca, and Sandyawan remained recognized comparators. The analytical output linked controls, enforcement points, and evidence; an additional application sector or the word governance alone would not establish a distinct contribution.

## Interpretation boundaries

The comparison identifies who decides, which data, operations, and recipients a permission covers, and where the decision takes effect. It adds no measurements of data utility, FHE cost, or operational control effectiveness.

Service invocation, evaluation of publicly available ciphertexts, and authorization of decryption or release are distinct controls. Evaluation elsewhere is possible when ciphertexts and public evaluation material are available. An interface permission therefore does not establish a general prohibition on all unauthorized computation. An audit history and evidence that a specified computation is correct support different claims.

The synthesis supplies comparison criteria and proposed evaluation questions. It does not implement a system, determine a unique cryptographic choice, replace experiments, or validate untested properties. SSI/DID/VC and computation verification must not be attributed to a system merely because they appear in the survey. Computation auditing does not establish regulatory certification, measurement truth, or every subsequent processing purpose.

## Historical preservation and checks

The preceding manuscript snapshot was `main-before-architecture-synthesis.tex`. The historical source-preparation records `architecture-synthesis-preservation-before.json` and `architecture-synthesis-validation.json` recorded extraction and dataset fingerprints and comparison of the existing tables with that snapshot. The requirement table was an analytical synthesis rather than a change to extracted results.

At that stage, source preparation used `export_and_validate.py`, `build_updated_dataset.py`, and `validate_updated_dataset.py`; the resulting export retained 106 records. These names document the historical preparation, not commands for rebuilding this repository. The portable dataset entry point is [run.py](../../../run.py). PDF inspection was recorded separately and did not constitute scientific validation.
