---
layout: default
---

# Design

- **Objective:** Develop a decentralized, secure, and transparent system for agricultural traceability using Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs).
- **Core Technology:** ACA-PY (Aries Cloud Agent Python) for identity management and DIDComm protocol for secure communication.
- **Key Components:** ACA-PY Agents, Bifold Wallet, Backend Services, AATP API, Web Application, and optional Blockchain Network.

---
layout: center
---

# Architecture
<img src="/assets/architecture.png" style="max-width: 70%;" alt="architecture" />

---
layout: two-cols-header
---

# Key Features of DID 

::left::

- **DIDs (Decentralized Identifiers):**
  - **Self-Sovereignty:** User-controlled without centralized authorities.
  - **Interoperability:** Built on W3C standards for compatibility across systems.
  - **Privacy:** Supports selective disclosure of data.
  - **Verifiability:** Cryptographically secure with public keys.
  - **DID Methods:** Use DID methods such as `did:sov` or `did:key` for different resolution mechanisms. Define the methods, including the resolver operations, and how DIDs are managed within the AATP system.

::right::

- **Example DID Document:**
  ```json
  {
    "@context": "https://www.w3.org/ns/did/v1",
    "id": "did:sov:123456789abcdefghi",
    "authentication": [
      {
        "id": "did:sov:123456789abcdefghi#keys-1",
        "type": "Ed25519VerificationKey2018",
        "controller": "did:sov:123456789abcdefghi",
        "publicKeyBase58": "H3C2AVvLMz...AB"
      }
    ],
    "service": [
      {
        "id": "did:sov:123456789abcdefghi#agent",
        "type": "DIDCommMessaging",
        "serviceEndpoint": "https://example.com/endpoint",
        "routingKeys": ["did:sov:123456789abcdefghi#keys-1"]
      }
    ]
  }
  ```

---
layout: two-cols-header
---

# Key Features of VC 

::left::
- **VCs (Verifiable Credentials):**
  - **Data Integrity:** Signed by the issuer’s private key to prevent tampering.
  - **Selective Disclosure:** Allows minimal data sharing.
  - **Interoperability:** W3C standard-based for wide usage.
  - **Revocation:** Supports revocation by the issuer, ensuring robust credential lifecycle management.
::right::
  **Example Verifiable Credential:**
  ```json
  {
    "@context": [
      "https://www.w3.org/2018/credentials/v1",
      "https://example.com/agriculture/credentials/v1"
    ],
    "id": "http://example.com/credentials/1872",
    "type": ["VerifiableCredential", "OrganicCertificationCredential"],
    "issuer": "did:sov:123456789abcdefghi",
    "issuanceDate": "2024-09-01T19:23:24Z",
    "credentialSubject": {
      "id": "did:sov:0987654321abcdefgh",
      "name": "Farmer John",
      "certification": "Organic Certification",
      "validUntil": "2025-09-01T00:00:00Z"
    },
    "proof": { ... }
  }
  ```

---
layout: two-cols-header
---

# System Architecture Components
- **ACA-PY Agents:** Manage decentralized identities and credentials, supporting DID management, credential issuance, verification, and revocation.
- **Bifold Wallet:** A digital wallet solution for users to manage decentralized identities and credentials securely. The Bifold Wallet can be customized beyond the scope of this project if required, providing flexibility for future expansions.
- **AATP API:** Manages the issuance, storage, and retrieval of digital product credentials, ensuring authenticity and data integrity in a decentralized manner. The AATP API includes endpoints for credential management (issue, verify, revoke, update), DID management, and querying credentials.

---
layout: default
---

# Use Case 1: Credential Issuance by Producers

- **Scenario:** A farmer requests a verifiable credential (VC) for their organic certification using the DI Wallet (Lissi Wallet).
- **Flow:**
  1. The farmer initiates a credential issuance request via the DI Wallet.
  2. The request is sent to the Passport API, which interfaces with the ACA-PY agent to issue the credential.
  3. The credential is digitally signed by the issuer’s ACA-PY agent and stored in the farmer’s DI Wallet.

---

# Use Case 2: Credential Verification Flow

- **Scenario:** A retailer verifies the authenticity of an organic certification before purchasing agricultural products.
- **Flow:**
  1. The retailer receives the credential from the supplier via DIDComm.
  2. The retailer submits the credential to the VDR API for verification.
  3. The VDR API, in conjunction with ACA-PY, checks the credential’s digital signature and revocation status, returning the verification result to the retailer.

---

# Use Case 3: Product Traceability for Consumers

- **Scenario:** A consumer wants to verify the sustainability credentials of a product before making a purchase.
- **Flow:**
  1. The consumer scans a QR code on the product packaging using the DI Wallet.
  2. The DI Wallet sends a verification request to the VDR API.
  3. The VDR API verifies the credentials associated with the product’s digital passport and returns the result to the consumer’s DI Wallet.

---

# Use Case 4: Regulatory Compliance Checks

- **Scenario:** A regulatory body conducts a compliance check to ensure a product meets local food safety standards.
- **Flow:**
  1. The regulator requests compliance credentials from the DI Wallet of the producer.
  2. The credentials are sent to the VDR API for validation.
  3. The VDR API verifies the credentials and provides the compliance status to the regulators.

---

# Use Case 5: Decentralized Credential Sharing

- **Scenario:** Credentials are directly shared between stakeholders (e.g., farmer to retailer) using secure DIDComm communication channels.
- **Flow:**
  1. The credential holder (farmer) uses the DI Wallet to share a credential with a retailer.
  2. The retailer’s DI Wallet receives the credential and verifies it using the VDR API.
  3. Secure communication is maintained throughout the process using DIDComm, ensuring data integrity and privacy.

---

# Use Case 6: Emergency Recall Notifications

- **Scenario:** A product recall is initiated due to contamination, and all related credentials must be revoked.
- **Flow:**
  1. The recall is initiated by the issuing authority, which updates the credential status in the DI Wallet.
  2. The recall status is communicated to all stakeholders via the VDR API.
  3. All stakeholders are notified through their DI Wallets, and the affected credentials are marked as revoked.

---
layout: cover
---

# Implementation plan

---
layout: default
---

# **aatp-core-services**
- **Objective:** Consolidate all core backend services and components required for the AATP system, including ACA-PY agents, API services, DID management, and optional blockchain integration.
- **Components Included:**
  - ACA-PY agents for decentralized identity and credential management.
  - Backend APIs for credential issuance, verification, revocation, and DID operations.
  - DID management tools, compliant with W3C DID specifications (creation, resolution, updates, deactivation).
  - Optional blockchain integration to provide an immutable ledger for DID anchoring and credential transactions.

---
layout: default
---

# **aatp-mobile-app**
 - **Objective:** Develop a customized mobile application based on the Bifold Wallet, tailored to AATP-specific use cases for managing credentials, performing selective disclosure, and scanning QR codes.
 - **Components Included:**
   - Customized Bifold Wallet for mobile users.
   - QR code scanning functionality for verifying product credentials.
   - User-friendly mobile interface for managing decentralized identities and credentials.

---
layout: default
---

# **aatp-web-app**
 - **Objective:** Build a web-based application to enable stakeholders to interact with the AATP system from a desktop interface, manage credentials, perform verification checks, and view dashboards.
 - **Components Included:**
   - User interface for credential management and verification.
   - Dashboard for monitoring issued and received credentials.
   - Integration with the AATP core services for backend operations.

---
layout: default
---
# **aatp-compliance-testing-and-docs**
   - **Objective:** Merge compliance tools, governance scripts, integration testing, and documentation into one repository to ensure the system meets regulatory standards, functions reliably, and provides clear guidance for deployment and use.
   - **Components Included:**
     - Scripts and tools for governance, compliance checks, and audit processes.
     - Integration testing suite to validate the functionality and interoperability of all AATP components.
     - Comprehensive documentation, including setup guides, API documentation, and user manuals.
     - Demo scripts and sample data to showcase various use cases (credential issuance, verification, traceability, and compliance workflows).
