
# Regulatory Compliance Checks
**Objective:** Enable regulatory bodies to conduct compliance checks.

## Actors
- Regulatory Bodies
- Producers

## Request Compliance Credentials
Regulator requests compliance credentials via ACA-PY agent using the web application.

## Present Compliance Credentials
Producer sends credentials using Bifold Wallet.

## Mutual Authentication
Ensure that the regulatory body authenticates itself to the producer’s agent using mutual DIDComm authentication.

## Verify Compliance
Regulator’s agent verifies credentials with AATP API, ensuring they meet the required standards.

## Generate Compliance Report
Regulator generates a compliance report based on verification.

## Notify Producer
Producer is notified of the compliance check outcome.
