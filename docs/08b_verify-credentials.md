
# Credential Verification by Retailers
**Objective:** Enable retailers to verify the authenticity of certifications before purchasing products.

## Actors
- Retailers
- Producers

## Connect to Producer
Retailer establishes a DIDComm connection with the producer’s agent.

## Request Credential Presentation
Retailer requests credential presentation via DIDComm using the web application.

## Present Credential
Producer sends the credential using Bifold Wallet.

## Verify Credential
Retailer’s agent uses AATP API for verification, ensuring the credential adheres to the W3C VC standards.

## Cache Verification Result
Retailer’s agent caches the verification result to optimize performance for repeated checks.

## Receive Verification Result
Retailer receives the verification result confirming authenticity.
