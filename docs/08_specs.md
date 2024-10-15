# Specifications

## Credential Issuance by Producers
**Objective:** Allow producers to request and receive verifiable credentials (VCs) for certifications.

### Implementation Steps:
1. **Set Up ACA-PY Agents:** Deploy ACA-PY agents for both the credential issuer (e.g., certification body) and the producer.
2. **Create DIDs:** Generate Decentralized Identifiers (DIDs) for both issuer and producer. Register these DIDs on the appropriate network or ledger.
3. **Credential Definition and Schema:** Define a credential schema on the ledger for the type of certification, ensuring compliance with the W3C VC Data Model.
4. **Onboard Producer:** Register producer's DID with the issuer’s agent; connect using Bifold Wallet.
5. **Request Credential:** Producer uses the web application to request a credential, submitting necessary data.
6. **Issue Credential:** Issuer verifies details, issues a signed credential to the producer’s agent, and registers it with the AATP API.
7. **Store Credential:** Producer stores the credential in Bifold Wallet.
8. **Confirm Receipt:** Producer confirms receipt of the credential.
9. **Credential Revocation Process:** Include a process for revoking credentials if certifications are withdrawn or incorrectly issued, ensuring the AATP API is updated accordingly.

## Credential Verification by Retailers
**Objective:** Enable retailers to verify the authenticity of certifications before purchasing products.

### Implementation Steps:
1. **Set Up ACA-PY Agents:** Deploy ACA-PY agents for the retailer.
2. **Connect to Producer:** Retailer establishes a DIDComm connection with the producer’s agent.
3. **Request Credential Presentation:** Retailer requests credential presentation via DIDComm using the web application.
4. **Present Credential:** Producer sends the credential using Bifold Wallet.
5. **Verify Credential:** Retailer’s agent uses AATP API for verification, ensuring the credential adheres to the W3C VC standards.
6. **Cache Verification Result:** Retailer’s agent caches the verification result to optimize performance for repeated checks.
7. **Receive Verification Result:** Retailer receives the verification result confirming authenticity.

## Product Traceability for Consumers
**Objective:** Allow consumers to verify product sustainability credentials via QR codes.

### Implementation Steps:
1. **Set Up ACA-PY Agents:** Deploy ACA-PY agents for both producer and consumer.
2. **Register Product Credentials:** Producer registers digital product passport credentials on AATP API.
3. **Generate QR Code:** Generate a QR code with product DID and attach it to packaging. Ensure the DID is not easily guessable to prevent unauthorized access.
4. **Consumer Scans QR Code:** Consumer scans the QR code using Bifold Wallet.
5. **Request Verification:** Consumer’s wallet requests verification from AATP API.
6. **Verify Product Credentials:** AATP API verifies credentials and returns the result.
7. **Display Verification Status:** Consumer's wallet displays the verification result.

## Regulatory Compliance Checks
**Objective:** Enable regulatory bodies to conduct compliance checks.

### Implementation Steps:
1. **Set Up ACA-PY Agents:** Deploy ACA-PY agents for both the regulatory body and producers.
2. **Request Compliance Credentials:** Regulator requests compliance credentials via ACA-PY agent using the web application.
3. **Present Compliance Credentials:** Producer sends credentials using Bifold Wallet.
4. **Mutual Authentication:** Ensure that the regulatory body authenticates itself to the producer’s agent using mutual DIDComm authentication.
5. **Verify Compliance:** Regulator’s agent verifies credentials with AATP API, ensuring they meet the required standards.
6. **Generate Compliance Report:** Regulator generates a compliance report based on verification.
7. **Notify Producer:** Producer is notified of the compliance check outcome.

## Decentralized Credential Sharing
**Objective:** Enable secure, direct sharing of credentials between stakeholders.

### Implementation Steps:
1. **Set Up ACA-PY Agents:** Deploy ACA-PY agents for both the credential holder (e.g., farmer) and the verifier (e.g., retailer).
2. **Establish DIDComm Connection:** Secure DIDComm connection established between stakeholders using DIDComm messaging patterns (e.g., one-to-one, broadcast).
3. **Initiate Credential Sharing:** Credential holder uses Bifold Wallet to share the credential.
4. **Send Credential:** Credential sent via DIDComm to the verifier’s agent.
5. **Credential Verification:** Verifier’s agent verifies the credential with AATP API.
6. **Acknowledge Receipt:** Verifier confirms receipt and verification of the credential.

## Emergency Recall Notifications
**Objective:** Manage product recalls and revoke related credentials.

### Implementation Steps:
1. **Set Up ACA-PY Agents:** Deploy ACA-PY agents for the issuing authority and stakeholders.
2. **Initiate Recall:** Issuing authority initiates recall using the web application and updates credential status.
3. **Update Credential Status:** Credentials marked as revoked in AATP API.
4. **Notify Stakeholders:** All stakeholders are notified via DIDComm. Define clear messaging protocols for efficient recall communication.
5. **Acknowledge Recall:** Stakeholders confirm receipt and update their systems.
6. **Ensure Revocation:** AATP API confirms revocation status, ensuring all credentials are invalidated.
7. **Monitor Compliance:** Issuing authority monitors compliance with recall procedures, using DIDComm for secure and efficient updates.
