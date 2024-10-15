import argparse
import requests
import json  # Import json for pretty printing

API_URL = "https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiI4YWUxNDI0Ni0wODJhLTRmOTYtYTc2Zi05N2UyZmVjOTkwNGUiLCJpYXQiOjE3Mjg5MDAzMzMsImV4cCI6MTcyODk4NjczM30.SMhv3HERow_2eDPPRMzG7QK0gZs-iGNMAF4XbKj42Ps"

def send_api_call(url, method='GET', headers=None, data=None, debug=False):
    try:
        if debug:
            # Print args before sending request
            print("Request details:")
            print(f"Method: {method}")
            print(f"URL: {url}")
            print("Headers:")
            for key, value in headers.items():
                print(f"  {key}: {value}")
            print("Data:")
            print(json.dumps(data, indent=2))
            print("\nSending request...")
        
        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
        print(f"Response content: {response.text}")
        raise

def create_schema(schema_name, schema_version, attributes, auth_token=AUTH_TOKEN, url=API_URL, debug=False):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data = {
        "schema_name": schema_name,
        "schema_version": schema_version,
        "attributes": attributes
    }
    
    try:
        response = send_api_call(f"{url}/schemas", method='POST', headers=headers, data=data, debug=debug)
        print("Schema created:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error creating schema: {e}")

def create_credential_definition(schema_id, tag, support_revocation=False, auth_token=AUTH_TOKEN, url=API_URL, debug=False):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data = {
        "schema_id": schema_id,
        "tag": tag,
        "support_revocation": support_revocation
    }
    
    try:
        response = send_api_call(f"{url}/credential-definitions", method='POST', headers=headers, data=data, debug=debug)
        print("Credential definition created:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error creating credential definition: {e}")

def interactive_create_schema(debug=False):
    schema_name = input("Enter schema name: ")
    schema_version = input("Enter schema version: ")
    attributes = input("Enter attributes (comma-separated): ").split(',')
    attributes = [attr.strip() for attr in attributes]
    create_schema(schema_name, schema_version, attributes, debug=debug)

def interactive_create_credential_definition(debug=False):
    schema_id = input("Enter schema ID: ")
    tag = input("Enter tag for credential definition: ")
    support_revocation = input("Support revocation? (true/false): ").lower() == 'true'
    create_credential_definition(schema_id, tag, support_revocation, debug=debug)

def main():
    parser = argparse.ArgumentParser(description='A command line utility for demonstrating Australian Agricultural Traceability Protocol.')
    parser.add_argument('--create-schema', action='store_true', help='Create a new schema.')
    parser.add_argument('--create-cred-def', action='store_true', help='Create a new credential definition.')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode.')
    parser.add_argument('--schema-name', type=str, help='Name of the schema to create.')
    parser.add_argument('--schema-version', type=str, help='Version of the schema to create.')
    parser.add_argument('--attributes', type=str, nargs='+', help='List of attributes for the schema.')
    parser.add_argument('--schema-id', type=str, help='Schema ID for creating credential definition.')
    parser.add_argument('--tag', type=str, help='Tag for the credential definition.')
    parser.add_argument('--support-revocation', action='store_true', help='Enable support for revocation in credential definition.')
    parser.add_argument('--auth-token', type=str, default=AUTH_TOKEN, help='Authorization token for API calls.')
    parser.add_argument('--url', type=str, default=API_URL, help='URL for the API endpoint.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode to print request details.')

    args = parser.parse_args()

    if args.interactive:
        action = input("Choose action (create-schema/create-cred-def): ").lower()
        if action == 'create-schema':
            interactive_create_schema(debug=args.debug)
        elif action == 'create-cred-def':
            interactive_create_credential_definition(debug=args.debug)
        else:
            print("Invalid action. Please choose 'create-schema' or 'create-cred-def'.")
    elif args.create_schema:
        if not args.schema_name or not args.schema_version or not args.attributes:
            print("Error: --schema-name, --schema-version, and --attributes are required.")
            parser.print_help()
        else:
            create_schema(args.schema_name, args.schema_version, args.attributes, auth_token=args.auth_token, url=args.url, debug=args.debug)
    elif args.create_cred_def:
        if not args.schema_id or not args.tag:
            print("Error: --schema-id and --tag are required for creating a credential definition.")
            parser.print_help()
        else:
            create_credential_definition(args.schema_id, args.tag, args.support_revocation, auth_token=args.auth_token, url=args.url, debug=args.debug)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

# Create a schema
# python aatp.py --create-schema --schema-name "agri_producer" --schema-version "1.4" --attributes "producer_name" "producer_id" "location" "certification_status" "contact_info" --debug
# Create a credential definition
# python aatp.py --create-cred-def --schema-id "VDbghfvE6dGvgA5dK9p1DC:2:agri_producer:1.0" --tag "AgriProducer" --debug
# Interactive mode
# python aatp.py --interactive --debug