# Issue credentials
**Objective:** Allow producers to request and receive verifiable credentials (VCs) for certifications.

## Actors
- Producer
- Issuer

## **Create DIDs
Generate Decentralized Identifiers (DIDs) for both issuer and producer. Register these DIDs on the appropriate network or ledger.

## Credential Definition and Schema
Define a credential schema on the ledger for the type of certification, ensuring compliance with the W3C VC Data Model.

## Onboard Producer
Register producer's DID with the issuer’s agent; connect using Aries-compatible Wallet.

## Request Credential
Producer uses the web application to request a credential, submitting necessary data.

## Issue Credential
Issuer verifies details, issues a signed credential to the producer’s agent, and registers it with the AATP API.

## Store Credential
Producer stores the credential in Aries-compatible Wallet.

## Confirm Receipt
Producer confirms receipt of the credential.

## Credential Revocation Process
Include a process for revoking credentials if certifications are withdrawn or incorrectly issued, ensuring the AATP API is updated accordingly.

curl -X POST 'https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/issue-credential/send' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiIyYzA4MDE0MC0yYzVkLTRkMTAtOWE0YS00NzUwZmU5YTc2ODkiLCJpYXQiOjE3Mjg5ODM0OTAsImV4cCI6MTcyOTA2OTg5MH0.8YN82ZnAvDnV8_QmCKvyK5XL_xY5TJyIjF-kC-NBojA' \
-H 'Content-Type: application/json' \
-d '{
  "connection_id": "CONNECTION_ID", 
  "credential_definition_id": "VDbghfvE6dGvgA5dK9p1DC:3:CL:123:tag",
  "credential_proposal": {
    "credential_definition_id": "VDbghfvE6dGvgA5dK9p1DC:3:CL:123:tag",
    "attributes": [
      "producer_name",
      "producer_id",
      "location",
      "certification_status",
      "contact_info"
    ]
  },
  "credential_values": {
    "producer_name": "John Doe",
    "producer_id": "123456789",
    "location": "New York, USA",
    "certification_status": "Certified Organic",
    "contact_info": "john.doe@example.com"
  },
  "comment": "Requesting Agri Producer credential",
  "auto_issue": true
}'
