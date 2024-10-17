# Issue credentials
**Objective:** Allow producers to request and receive verifiable credentials (VCs) for certifications.

## Actors
- Producer
- Issuer

## Create Schema and Credential Definition for Producer and Issuer


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

d1eefc99-d0d7-49b5-885e-909306cab31d