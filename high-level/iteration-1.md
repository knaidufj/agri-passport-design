# Decentralized System Architecture for Demonstrating Australian Agricultural Traceability Protocol (AATP)

Leveraging ACA-PY Lissi Wallet and W3C Verifiable Credentials for Secure and Transparent Agricultural Supply Chains

## Concept - Iteration 1 (30 Aug 2024)

---

### Technical Overview of AATP Decentralized Architecture

- **Objective:** Implement a decentralized, secure, and transparent system for agricultural traceability using Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs).
- **Core Technology:** Utilizes ACA-PY (Aries Cloud Agent Python), a framework from the Hyperledger Aries project, to manage identities and credentials via the DIDComm protocol, ensuring secure peer-to-peer communication.
- **Key Components:** ACA-PY Agents, Backend Services, DI Wallet (Lissi Wallet), and Web Application.

---

### DIDs - Key Features

- **Self-Sovereignty:** DIDs are controlled by the DID subject without relying on a centralized registry, identity provider, or certificate authority.
- **Interoperability:** Built on open standards defined by the W3C, DIDs are designed to be interoperable across different systems and networks.
- **Privacy-Enhancing:** DIDs provide a high level of privacy by minimizing the data shared during interactions and supporting selective disclosure where only the necessary information is shared.
- **Cryptographically Verifiable:** Each DID document contains a set of public keys and service endpoints that can be used for verification purposes.

---

### How DIDs Work

1. A DID is associated with a DID document, which contains information such as public keys and endpoints for services where the DID can be used.
2. The DID document is stored on a decentralized network or distributed ledger.
3. The DID can be resolved to its DID document using a DID resolver, which is a software component that can retrieve the DID document from the ledger or network.

---

### Verifiable Credentials (VCs)

- **Definition:** Verifiable Credentials (VCs) are digital assertions that are cryptographically secure, privacy-respecting, and can be used to prove specific attributes about a person, organization, or thing. VCs are issued by trusted entities (issuers) and are designed to be tamper-evident and verifiable anywhere.

---

### VCs - Key Features

- **Data Integrity:** VCs are signed by the issuer’s private key, ensuring that any tampering with the credential after issuance is detectable.
- **Selective Disclosure:** VCs allow holders to share only the necessary data with verifiers, protecting user privacy.
- **Interoperability:** VCs are based on W3C standards, making them interoperable across different systems and platforms.
- **Revocation Support:** VCs can be revoked by the issuer if needed, ensuring that credentials are always up-to-date.

---

### How VCs Work

1. A VC consists of three parties: the issuer (who issues the credential), the holder (who holds the credential), and the verifier (who verifies the credential’s authenticity).
2. The issuer signs the credential with their private key and gives it to the holder.
3. The holder can present the credential to a verifier to prove a certain claim (e.g., age, membership).
4. The verifier checks the credential’s digital signature and optionally verifies the credential status (e.g., revocation status).

---

### DIDComm Protocol

- **Definition:** DIDComm is a protocol for secure and private communication between decentralized identities (DIDs). It provides a way for entities to communicate peer-to-peer without requiring a centralized intermediary, enabling a range of secure interactions such as data exchange, credential issuance, and verification.

---

### DIDComm Protocol - Key Features

- **End-to-End Encryption:** Ensures that messages are encrypted from sender to receiver, preventing any third party from intercepting the communication.
- **Interoperability:** Built to work seamlessly with DIDs and verifiable credentials, enabling secure communication across different systems and networks.
- **Peer-to-Peer Communication:** Allows entities to interact directly without the need for a centralized server, improving privacy and reducing dependency on intermediaries.
- **Extensibility:** Supports a variety of message types and communication patterns, allowing for flexible application in different scenarios such as credential issuance, identity proofing, and secure data exchange.

---

### How DIDComm Works

1. DIDComm uses a combination of DID Documents, public key cryptography, and messaging protocols to establish secure channels between entities.
2. A DIDComm message is constructed by encrypting the payload with the recipient’s public key (found in the recipient’s DID Document) and signing it with the sender’s private key.
3. The message is then sent directly to the recipient, who decrypts it using their private key and verifies the signature using the sender’s public key.
4. DIDComm supports multiple messaging patterns, including one-to-one, one-to-many, and many-to-many communications.

---

### Comparison of Decentralized, Centralized, and Blockchain Architectures

| Feature              | Decentralized Architecture                                                                 | Centralized Architecture                                              | Blockchain Architecture                                                |
|----------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------|
| **Control**          | Distributed; each node operates independently using agents like ACA-PY to manage identities and credentials. | Centralized control under a single entity or server.                  | Distributed control across nodes; consensus-based decisions required for changes. |
| **Security**         | High security with peer-to-peer encryption and no single point of failure. Uses DIDComm for secure messaging. | Vulnerable to breaches at central points; weaker overall security due to reliance on a single point of trust. | High security due to blockchain's immutability and consensus mechanisms; performance can be a trade-off. |
| **Data Privacy**     | User-controlled data; minimal exposure with decentralized data sharing using DIDs and VCs.  | Centralized data storage often leads to overexposure and data leakage risks. | Data transparency is high but privacy may be compromised as all transactions are visible on the ledger. |
| **Scalability**      | Highly scalable; nodes can be added or removed without affecting overall system integrity.   | Limited by central server capacity and bandwidth; scaling is costly and complex. | Scalability is challenging; blockchain size and transaction volume can impact performance. |
| **Interoperability** | Built on open standards (W3C); easily integrates with various systems and platforms.         | Often relies on proprietary standards, making interoperability difficult. | Depends on blockchain type; public blockchains may have limited interoperability with non-blockchain systems. |
| **Data Integrity**   | Ensured by cryptographic verification and decentralized storage; credentials are tamper-proof and verifiable. | Data integrity is dependent on central server integrity; higher risk of data tampering. | Data integrity is inherently high due to blockchain immutability; once data is written, it cannot be altered. |
| **Cost**             | Lower infrastructure costs; no need for a central server; decentralized model reduces operational overhead. | Higher infrastructure and maintenance costs; requires robust central servers and security measures. | High initial and ongoing costs due to the complexity of maintaining a distributed ledger. |

---

### Core Components of AATP Decentralized System

- **ACA-PY Agents:** Serve as the foundation for decentralized identity and credential management.
- **Passport API:** Interacts with ACA-PY to issue credentials.
- **Verifiable Data Registry (VDR API):** Works with ACA-PY to verify and store credentials.
- **DI Wallet (Lissi Wallet):** A digital wallet solution for users to manage decentralized identities and credentials.
- **Web Application:** GUI-based tool for demonstrating system functionalities.

---

### ACA-PY Background Operations

- **Role of ACA-PY:** Provides a decentralized infrastructure for managing digital identities and credentials across all nodes.
- **Key Functions:**
  - DID Management
  - Credential Issuance and Verification
  - Peer-to-Peer Communication
- **Supports:** Various credential exchange protocols for enhanced interoperability.

---

### Passport API

- **Purpose:** Manage the issuance, storage, and retrieval of digital product passports for agricultural products.
- **Key API Endpoints:**
  - `POST /product-passport`: Create a new product passport.
  - `GET /product-passport/{id}`: Retrieve details of a specific product passport.
  - `PUT /product-passport/{id}`: Update an existing product passport.
  - `DELETE /product-passport/{id}`: Delete a product passport.
- **Use Cases:**
  - Issue product credentials like certifications and compliance documents.
  - Manage lifecycle updates and deletions of product passports.
- **Integration:** Works with ACA-PY for DID management and credential signing.

---

### VDR API

- **Purpose:** Verify and store credentials in a decentralized manner, ensuring authenticity and data integrity.
- **Key API Endpoints:**
  - `POST /credentials`: Issue a new credential linked to a product passport.
  - `GET /credentials/{id}`: Retrieve details of a specific credential.
  - `PUT /credentials/{id}`: Update an existing credential.
  - `DELETE /credentials/{id}`: Remove a credential from the system.
- **Use Cases:**
  - Verify product credentials for authenticity and validity.
  - Manage credential lifecycle, including issuance, updates, and revocation.
- **Integration:** Communicates with ACA-PY for secure verification and credential management.

---

### Decentralized Identity Wallet (Lissi Wallet)

- **User Interaction:** End-Users like Farmers, regulators, and consumers use Lissi Wallet for credential management.
- **Credential Management:** Supports creating, verifying, receiving, and managing credentials.
- **Integration with Backend Services:** Communicates with Passport API and VDR API through ACA-PY agents for credential operations.

---

### Web Application for GUI-Based Demonstration

- **Purpose:** Provides a graphical user interface to demonstrate decentralized system functionalities.
- **Interactions:** With Lissi Wallet for user interactions and with backend services for credential operations.

---

### Optional and Additional Systems

- **Blockchain Network (Optional):** Provides an immutable ledger for anchoring DIDs and storing credential transactions.
- **External Compliance Systems:** Third-party systems or APIs interacting with Passport API or VDR API.

---

### Use Case Diagrams and Scenarios

#### Use Case 1: Credential Issuance by Producers

- **Scenario:** A farmer requests a verifiable credential (VC) for their organic certification using the DI Wallet (Lissi Wallet).
- **Flow:**
  1. The farmer initiates a credential issuance request via the DI Wallet.
  2. The request is sent to the Passport API, which interfaces with the ACA-PY agent to issue the credential.
  3. The credential is digitally signed by the issuer’s ACA-PY agent and stored in the farmer’s DI Wallet.

#### Use Case 2: Credential Verification Flow

- **Scenario:** A retailer verifies the authenticity of an organic certification before purchasing agricultural products.
- **Flow:**
  1. The retailer receives the credential from the supplier via DIDComm.
  2. The retailer submits the credential to the VDR API for verification.
  3. The VDR API, in conjunction with ACA-PY, checks the credential’s digital signature and revocation status, returning the verification result to the retailer.

#### Use Case 3: Product Traceability for Consumers

- **Scenario:** A consumer wants to verify the sustainability credentials of a product before making a purchase.
- **Flow:**
  1. The consumer scans a QR code on the product packaging using the DI Wallet.
  2. The DI Wallet sends a verification request to the VDR API.
  3. The VDR API verifies the credentials associated with the product’s digital passport and returns the result to the consumer’s DI Wallet.

#### Use Case 4: Regulatory Compliance Checks

- **Scenario:** A regulatory body conducts a compliance check to ensure a product meets local food safety standards.
- **Flow:**
  1. The regulator requests compliance credentials from the DI Wallet of the producer.
  2. The credentials are sent to the VDR API for validation.
  3. The VDR API verifies the credentials and provides the compliance status to the regulators.

#### Use Case 5: Decentralized Credential Sharing

- **Scenario:** Credentials are directly shared between stakeholders (e.g., farmer to retailer) using secure DIDComm communication channels.
- **Flow:**
  1. The credential holder (farmer) uses the DI Wallet to share a credential with a retailer.
  2. The retailer’s DI Wallet receives the credential and verifies it using the VDR API.
  3. Secure communication is maintained throughout the process using DIDComm, ensuring data integrity and privacy.

#### Use Case 6: Emergency Recall Notifications

- **Scenario:** A product recall is initiated due to contamination, and all related credentials must be revoked.
- **Flow:**
  1. The recall is initiated by the issuing authority, which updates the credential status in the DI Wallet.
  2. The recall status is communicated to all stakeholders via the VDR API.
  3. All stakeholders are notified through their DI Wallets, and the affected credentials are marked as revoked.

---

### Diagrams

- **Activity Diagrams:** For each use case scenario to illustrate the flow of operations.
- **Sequence Diagrams:** To show the sequence of messages and interactions between system components.
- **Component Diagrams:** To depict the architecture of the decentralized system and its core components.

---

### Feedback:
- Clear distinction between decentralised and blockchain approach needs to be made.
- Lissi Wallet does not support app customisations that may be required for the system.
- Web app cannot just be an additional demo app, it needs to act as an companion app for the user along with the mobile wallet to facilitate the use cases.
- Clear boundaries between Passport and VDR API are not defined.
- More clarity required on the use cases.