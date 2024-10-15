# API Calls

## Create a schema 

### Schema for Producer
```
curl -X POST "https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/schemas" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps" \
-H "Content-Type: application/json" \
-d '{
  "schema_name": "agri_producer",
  "schema_version": "1.0",
  "attributes": [
    "producer_name",
    "producer_id",
    "location",
    "certification_status",
    "contact_info"
  ]
}'
```

### Schema for Issuer
```
curl -X POST "https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/schemas" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps" \
-H "Content-Type: application/json" \
-d '{
  "schema_name": "agri_issuer",
  "schema_version": "1.0",
  "attributes": [
    "issuer_name",
    "issuer_id",
    "certification_type",
    "certification_status",
    "contact_info"
  ]
}'
```

### Schema for an example certification for Producer
```
curl -X POST "https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/schemas" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps" \
-H "Content-Type: application/json" \
-d '{
  "schema_name": "agri_certification",
  "schema_version": "1.0",
  "attributes": [
    "certification_type",
    "certification_status",
    "certification_date",
    "certification_expiration_date"
  ]
}'
```

## Create a credential definition

### Credential definition for Producer
```
curl -X POST 'https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/credential-definitions' \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps" \
-H 'Content-Type: application/json' \
-d '{
  "schema_id": "VDbghfvE6dGvgA5dK9p1DC:2:agri_producer:1.0",
  "tag": "AgriProducer",
  "support_revocation": false
}'
```


### Credential definition for Issuer
```
curl -X POST 'https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/credential-definitions' \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps" \
-H 'Content-Type: application/json' \
-d '{
  "schema_id": "VDbghfvE6dGvgA5dK9p1DC:2:agri_issuer:1.0",
  "tag": "AgriIssuer",
  "support_revocation": false
}'
```

## Create a connection

### Connection for Producer

```
curl -X POST 'https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/connections/create-invitation?multi_use=true' \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps" \
-H 'Content-Type: application/json' \
-d '{
  "alias": "AgriProducer",
  "auto_accept": true,
  "public": false
}'
```

### Connection for Issuer

```
curl -X POST 'https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca/connections/create-invitation?multi_use=true' \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps" \
-H 'Content-Type: application/json' \
-d '{
  "alias": "AgriIssuer",
  "auto_accept": true,
  "public": false
}'
```
