# DID, credentials, and wallet standards as of 1 October 2026

This targeted update uses official specifications, legislation, and versioned project documentation. It updates the SSI background and identity implementation comparison. These contextual sources are outside the 136 application records and the existing 67-record synthesis audit. Application eligibility, study identities, primary-text assessments, and search limitations are unchanged. This is not a new exhaustive search of digital-identity products or national identity laws.

## Specification status and source locations

| Reference | Status at the cutoff | Primary location and use |
|---|---|---|
| `bg-did-core` | W3C Recommendation, 19 July 2022 | [DID Core v1.0](https://www.w3.org/TR/2022/REC-did-core-20220719/), §§1.3, 7, 8–9. DID methods and registry options, controller/subject distinction, correlation risks. |
| `bg-did-11-2026` | Candidate Recommendation Snapshot, 5 March 2026 | [DID v1.1](https://www.w3.org/TR/2026/CR-did-1.1-20260305/), Status of This Document. Not a completed Recommendation. |
| `bg-vc-data-model-2` | W3C Recommendation, 15 May 2025 | [VC Data Model v2.0](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/), terminology, roles, securing mechanisms, trust model. DIDs are optional, and cryptographic verification does not establish claim truth. |
| `bg-vc-data-integrity2025`, `bg-vc-jose-cose2025` | W3C Recommendations, 15 May 2025 | [Data Integrity 1.0](https://www.w3.org/TR/2025/REC-vc-data-integrity-20250515/) and [JOSE/COSE](https://www.w3.org/TR/2025/REC-vc-jose-cose-20250515/), abstracts, conformance and securing rules. Separate securing specifications, not guarantees of anonymous presentation. |
| `platform-sdjwt-rfc9901` | Standards Track RFC, November 2025 | [RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html), §§3.3, 9.5, 10.1. Selected-claim disclosure and optional key binding. Reuse links presentations between verifiers, while issuer-verifier collusion can link a single presentation to issuance. |
| `platform-sdjwt-vc2026` | Internet-Draft 19, 31 August 2026 | [SD-JWT VC profile](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-sd-jwt-vc-19), status/header. Publication of the SD-JWT core RFC does not finalize this distinct credential profile. |
| `bg-vc-di-bbs-2026` | Candidate Recommendation Draft, 10 September 2026 | [BBS cryptosuite](https://www.w3.org/TR/2026/CRD-vc-di-bbs-20260910/), status, derived proofs, privacy considerations. Unlinkable cryptographic proofs do not hide identifying disclosed attributes or external metadata. |
| `platform-openid4vci2025`, `platform-openid4vp2025` | Final 1.0, 16 September and 9 July 2025 | [Issuance](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0-final.html) and [presentation](https://openid.net/specs/openid-4-verifiable-presentations-1_0-final.html), abstracts, formats, security/privacy considerations. Exchange protocols remain separate from credential-format privacy and issuer recognition. |
| `platform-haip2025` | Final 1.0, 24 December 2025 | [HAIP](https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-final.html), §§1, 3.4 and format profiles. Trust management is outside scope, and this profile alone is insufficient for eIDAS High assurance. |
| `platform-openid-conformance2026` | Self-certification opened, 7 August 2026 | [OpenID Foundation announcement](https://openid.net/openid4vp-and-openid4vci-conformance-tests-are-complete-and-open-for-self-certification/), profile and role coverage. No table entry is claimed certified from declared protocol support. |
| `platform-status-list2025` | W3C Recommendation, 15 May 2025 | [Bitstring Status List v1.0](https://www.w3.org/TR/2025/REC-vc-bitstring-status-list-20250515/), status, validation, caching and privacy. Signed status integrity and sufficiently fresh status are distinct checks. |

## Regulatory and architectural sources

- [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng), inserted eIDAS Articles 5a(2), 5a(4)(a), 5a(15–17), 5b(1–3) and 5c(1). Supports selective disclosure, conditional unlinkability where identification is unnecessary, relying-party registration and wallet certification. It does not mandate blockchain or DIDs, or certify the privacy of the reference code.
- [Commission Implementing Regulation (EU) 2026/1731](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32026R1731), 15 July 2026, OJ 22 July, Article 4 and Annexes XI–XII. Updates the 2024 issuance/presentation specifications, including adapted ETSI TS 119 472-2 V1.2.1 (2026-03), TS 119 472-3 V1.1.1 (2026-03), and ISO/IEC 18013-7:2025 Annex C references. Official indexed HTML was inspected when direct EUR-Lex access required JavaScript verification.
- [EUDI Architecture and Reference Framework v3.0.0](https://eudi.dev/3.0.0/main/), §§5.4.1, 5.4.4, 6.3.2.4, 6.4.2 and 6.6.3.7. ISO mobile-document and SD-JWT VC wallet support, optional W3C VCDM for non-qualified attestations, issuer trust, and relying-party registration. Registration describes intended uses and requested attributes and does not pre-authorize processing. Revocation checking is recommended rather than guaranteed in every presentation.

The [official ARF v3.0.0 release](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases/tag/v3.0.0) was published on 23 July 2026 at 19:10:17 UTC. Its tag resolves to commit `c64f2cbb19aee37c571c58af66d359c4d5be29c8`. This version is within the contextual cutoff.

Wallet approval is a technical choice in a disclosure workflow. It is not, by itself, valid legal consent, a lawful basis for processing, or proof that a recipient obeys its declared purpose. EUDI is included as a regulated comparison relevant to disclosure, identity assurance, and accountability, rather than being classified automatically as SSI. The manuscript makes no claim that all EUDI wallets already provide anonymous-credential or zero-knowledge proofs.

## Implementation evidence

- [Credo v0.7.0](https://github.com/openwallet-foundation/credo-ts/tree/b3d9bd7fa4482076bfc0d59495b5733575624d80), released 29 April 2026. Versioned README and release metadata declare DIDComm, OpenID4VC, AnonCreds and SD-JWT VC support. This does not establish compatibility with every Final 1.0 option or certification. The older v0.6.x OpenID feature documentation describes experimental support and earlier drafts; their exact versions are not transferred to v0.7.0.
- [EUDI Android reference wallet](https://github.com/eu-digital-identity-wallet/eudi-app-android-wallet-ui/tree/43f362d2a720edb6d37a356b6a51b52b32c61f25), Demo version 2026.09.42, released 10 September 2026. Pinned README sections Specifications Employed and Important things to know describe issuance/presentation, certificate-based trust, and demo defaults that need replacement. Availability of reference code is not wallet certification. GitHub release/tag metadata were checked through the official API.
- [AnonCreds specification](https://hyperledger.github.io/anoncreds-spec/), cryptographic operations, registry abstraction and privacy boundaries. No particular ledger is required. The table compares the project specification, not independently measured implementations.
- Existing Veramo, Identity.com and Sovrin references remain. Sovrin's January 2026 read-only notice is specific to that network. Serto, Evernym/Verity and Civic Pass remain in a short lifecycle paragraph, rather than occupying three rows as if they represented current equivalent products.

## Editorial and evidence limits

The generic issuer–holder–verifier figure was removed from the manuscript without deleting its source image. The roles remain explained in prose, while the released space is used for current standards and regulated wallet responsibilities. No new manuscript section or application table was added. URLs appear through bibliography references in the implementation table. Contextual standardization maturity, implementation support, cryptographic privacy, and regulatory duties remain separate evidence categories.

The contextual cutoff is 1 October 2026. The existing application search retains its 30 September 2026 publication cutoff. No new full PDF or unversioned vendor marketing claim was used to infer guarantees.
