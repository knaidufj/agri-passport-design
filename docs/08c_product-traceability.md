# Product Traceability for Consumers
**Objective:** Allow consumers to verify product sustainability credentials via QR codes.

## Actors
- Consumers
- Producers

## Register Product Credentials
Producer registers digital product passport credentials on AATP API.

## Generate QR Code
Generate a QR code with product DID and attach it to packaging. Ensure the DID is not easily guessable to prevent unauthorized access.

## Consumer Scans QR Code
Consumer scans the QR code using Bifold Wallet.

## Request Verification
Consumer’s wallet requests verification from AATP API.

## Verify Product Credentials
AATP API verifies credentials and returns the result.

## Display Verification Status
Consumer's wallet displays the verification result.