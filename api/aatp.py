import argparse
import requests
import json
import qrcode
import os

API_URL = "https://traction-sandbox-tenant-proxy.apps.silver.devops.gov.bc.ca"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXRfaWQiOiIyYzA4MDE0MC0yYzVkLTRkMTAtOWE0YS00NzUwZmU5YTc2ODkiLCJpYXQiOjE3MjkwODY1OTksImV4cCI6MTcyOTE3Mjk5OX0.XSo5Fn19F8xRhWk-aaMpAPjcJZ3hitLJHgmfpNY5OdQ"

def send_api_call(url, method='GET', headers=None, data=None):
    curl_command = f"curl -X {method} '{url}'"
    if headers:
        for key, value in headers.items():
            curl_command += f" \\\n-H '{key}: {value}'"
    if data:
        curl_command += f" \\\n-d '{json.dumps(data, indent=4)}'"
    print(curl_command)
    
    try:
        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
        print(f"Response content: {response.text}")
        raise

def check_status(auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "accept": "application/json"
    }
    
    try:
        response = send_api_call(f"{url}/status/ready", method='GET', headers=headers)
        print("Status checked:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error checking status: {e}")

def send_message(connection_id, content, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    data = {
        "content": content
    }
    
    try:
        response = send_api_call(f"{url}/connections/{connection_id}/send-message", method='POST', headers=headers, data=data)
        print("Message sent:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error sending message: {e}")

def query_messages(connection_id, state='sent', auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "accept": "application/json"
    }
    
    try:
        response = send_api_call(f"{url}/basicmessages?connection_id={connection_id}&state={state}", method='GET', headers=headers)
        print("Messages retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error querying messages: {e}")

def issue_credential(credential_data_path, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
    try:
        with open(credential_data_path, 'r') as file:
            credential_data = json.load(file)
        
        response = send_api_call(f"{url}/issue-credential-2.0/send", method='POST', headers=headers, data=credential_data)
        print("W3C Credential requested:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error requesting W3C credential: {e}")

def send_proposal(auto_remove, comment, connection_id, credential_preview, filter, replacement_id, trace, verification_method, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data = {
        "auto_remove": auto_remove,
        "comment": comment,
        "connection_id": connection_id,
        "credential_preview": credential_preview,
        "filter": filter,
        "replacement_id": replacement_id,
        "trace": trace,
        "verification_method": verification_method
    }
    
    try:
        response = send_api_call(f"{url}/issue-credential-2.0/send-proposal", method='POST', headers=headers, data=data)
        print("Proposal sent:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error sending proposal: {e}")

def create_schema(schema_name, schema_version, attributes, auth_token=AUTH_TOKEN, url=API_URL):
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
        response = send_api_call(f"{url}/schemas", method='POST', headers=headers, data=data)
        print("Schema created:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error creating schema: {e}")

def get_schema(schema_id, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "accept": "application/json"
    }
    
    try:
        response = send_api_call(f"{url}/schemas/{schema_id}", method='GET', headers=headers)
        print("Schema retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error retrieving schema: {e}")

def get_credential_definition(credential_definition_id, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "accept": "application/json"
    }
    
    try:
        response = send_api_call(f"{url}/credential-definitions/{credential_definition_id}", method='GET', headers=headers)
        print("Credential definition retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error retrieving credential definition: {e}")

def create_credential_definition(schema_id, tag, support_revocation=False, auth_token=AUTH_TOKEN, url=API_URL):
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
        response = send_api_call(f"{url}/credential-definitions", method='POST', headers=headers, data=data)
        print("Credential definition created:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error creating credential definition: {e}")

def create_invitation(alias, auto_accept=True, public=False, multi_use=True, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data = {
        "alias": alias,
        "auto_accept": auto_accept,
        "public": public
    }
    
    try:
        response = send_api_call(f"{url}/connections/create-invitation?multi_use={str(multi_use).lower()}", method='POST', headers=headers, data=data)
        print("Connection invitation created:\n", json.dumps(response, indent=4))
        
        # Get the invitation URL from the response
        invitation_url = response.get("invitation_url")
        print("Invitation URL:", invitation_url)

        # Show the URL as QR code image on Terminal 
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_code.add_data(invitation_url)
        qr_code.make(fit=True)
        img = qr_code.make_image(fill='black', back_color='white')

        # Display the QR code image in the terminal
        img.show()
        
        return response
    except Exception as e:
        print(f"Error creating connection invitation: {e}")

def query_active_connections(auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = send_api_call(f"{url}/connections", method='GET', headers=headers)
        print("Active connections:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error querying active connections: {e}")

def interactive_create_schema():
    schema_name = input("Enter schema name: ")
    schema_version = input("Enter schema version: ")
    attributes = input("Enter attributes (comma-separated): ").split(',')
    attributes = [attr.strip() for attr in attributes]
    create_schema(schema_name, schema_version, attributes)

def interactive_get_schema():
    schema_id = input("Enter schema ID to retrieve: ")
    get_schema(schema_id)

def interactive_get_credential_definition():
    credential_definition_id = input("Enter credential definition ID to retrieve: ")
    get_credential_definition(credential_definition_id)

def interactive_create_credential_definition():
    schema_id = input("Enter schema ID: ")
    tag = input("Enter tag for credential definition: ")
    support_revocation = input("Support revocation? (true/false): ").lower() == 'true'
    create_credential_definition(schema_id, tag, support_revocation)

def interactive_create_invitation():
    alias = input("Enter alias for the invitation: ")
    auto_accept = input("Auto accept connection? (true/false): ").lower() == 'true'
    public = input("Make invitation public? (true/false): ").lower() == 'true'
    multi_use = input("Allow multiple use of invitation? (true/false): ").lower() == 'true'
    create_invitation(alias, auto_accept, public, multi_use)

def interactive_send_message():
    connection_id = input("Enter connection ID to send message: ")
    content = input("Enter message content: ")
    send_message(connection_id, content)

def interactive_query_messages():
    connection_id = input("Enter connection ID to query messages: ")
    state = input("Enter message state (sent/received): ")
    query_messages(connection_id, state)

def main():
    parser = argparse.ArgumentParser(description='A command line utility for demonstrating Australian Agricultural Traceability Protocol.')
    
    # Main options
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode.')
    parser.add_argument('--auth-token', type=str, default=AUTH_TOKEN, help='Authorization token for API calls.')
    parser.add_argument('--url', type=str, default=API_URL, help='URL for the API endpoint.')

    # Sub-parsers for different actions
    subparsers = parser.add_subparsers(dest='action', help='Action to perform')

    # Create schema sub-parser
    parser_schema = subparsers.add_parser('create-schema', help='Create a new schema')
    parser_schema.add_argument('--schema-name', type=str, required=True, help='Name of the schema to create.')
    parser_schema.add_argument('--schema-version', type=str, required=True, help='Version of the schema to create.')
    parser_schema.add_argument('--attributes', type=str, nargs='+', required=True, help='List of attributes for the schema.')

    # Get schema sub-parser
    parser_get_schema = subparsers.add_parser('get-schema', help='Retrieve an existing schema')
    parser_get_schema.add_argument('--schema-id', type=str, required=True, help='ID of the schema to retrieve.')

    # Get credential definition sub-parser
    parser_get_cred_def = subparsers.add_parser('get-cred-def', help='Retrieve an existing credential definition')
    parser_get_cred_def.add_argument('--credential-definition-id', type=str, required=True, help='ID of the credential definition to retrieve.')

    # Create credential definition sub-parser
    parser_cred_def = subparsers.add_parser('create-cred-def', help='Create a new credential definition')
    parser_cred_def.add_argument('--schema-id', type=str, required=True, help='Schema ID for creating credential definition.')
    parser_cred_def.add_argument('--tag', type=str, required=True, help='Tag for the credential definition.')
    parser_cred_def.add_argument('--support-revocation', action='store_true', help='Enable support for revocation in credential definition.')

    # Create invitation sub-parser
    parser_invitation = subparsers.add_parser('create-invitation', help='Create a new connection invitation')
    parser_invitation.add_argument('--alias', type=str, required=True, help='Alias for the invitation.')
    parser_invitation.add_argument('--auto-accept', action='store_true', help='Auto accept the connection.')
    parser_invitation.add_argument('--public', action='store_true', help='Make the invitation public.')
    parser_invitation.add_argument('--multi-use', action='store_true', help='Allow multiple use of the invitation.')

    # Send proposal sub-parser
    parser_send_proposal = subparsers.add_parser('send-proposal', help='Send a credential proposal')
    parser_send_proposal.add_argument('--auto-remove', action='store_true', help='Automatically remove the proposal after it is sent.')
    parser_send_proposal.add_argument('--comment', type=str, required=True, help='Comment for the proposal.')
    parser_send_proposal.add_argument('--connection-id', type=str, required=True, help='Connection ID for the proposal.')
    parser_send_proposal.add_argument('--credential-preview', type=json.loads, required=True, help='JSON string of the credential preview.')
    parser_send_proposal.add_argument('--filter', type=json.loads, required=True, help='JSON string of the filter for the proposal.')
    parser_send_proposal.add_argument('--replacement-id', type=str, required=True, help='Replacement ID for the proposal.')
    parser_send_proposal.add_argument('--trace', action='store_true', help='Enable tracing for the proposal.')
    parser_send_proposal.add_argument('--verification-method', type=str, required=True, help='Verification method for the proposal.')

    # Request W3C credential sub-parser
    parser_request_w3c = subparsers.add_parser('issue-credential', help='Request a W3C credential')
    parser_request_w3c.add_argument('--credential-data-path', type=str, required=True, help='Path to the JSON file containing the credential data.')

    # Query active connections sub-parser
    parser_connections = subparsers.add_parser('query-connections', help='Query active connections')

    # Query messages sub-parser
    parser_query_messages = subparsers.add_parser('query-messages', help='Query messages for a specific connection')
    parser_query_messages.add_argument('--connection-id', type=str, required=True, help='Connection ID to query messages for.')
    parser_query_messages.add_argument('--state', type=str, default='sent', help='State of messages to query (sent/received).')

    # Send message sub-parser
    parser_send_message = subparsers.add_parser('send-message', help='Send a message to a specific connection')
    parser_send_message.add_argument('--connection-id', type=str, required=True, help='Connection ID to send the message to.')
    parser_send_message.add_argument('--content', type=str, required=True, help='Content of the message to send.')

    # Check status sub-parser
    parser_check_status = subparsers.add_parser('check-status', help='Check the status of the service')

    args = parser.parse_args()

    if args.interactive:
        action = input("\nChoose an action:\n" 
                       "1. Create Schema\n" 
                       "2. Get Schema\n" 
                       "3. Get Credential Definition\n"
                       "4. Create Credential Definition\n" 
                       "5. Create Invitation\n" 
                       "6. Send Proposal\n"
                       "7. Issue Credential\n"
                       "8. Query Active Connections\n"
                       "9. Query Messages\n"
                       "10. Send Message\n"
                       "11. Check Status\n"
                       "Please enter the action number: ").lower()
        
        if action == '1':
            interactive_create_schema()
        elif action == '2':
            interactive_get_schema()
        elif action == '3':
            interactive_get_credential_definition()
        elif action == '4':
            interactive_create_credential_definition()
        elif action == '5':
            interactive_create_invitation()
        elif action == '6':
            auto_remove = input("Auto remove? (true/false): ").lower() == 'true'
            comment = input("Enter comment for the proposal: ")
            connection_id = input("Enter connection ID: ")
            credential_preview = json.loads(input("Enter credential preview as JSON: "))
            filter = json.loads(input("Enter filter as JSON: "))
            replacement_id = input("Enter replacement ID: ")
            trace = input("Enable trace? (true/false): ").lower() == 'true'
            verification_method = input("Enter verification method: ")
            send_proposal(auto_remove, comment, connection_id, credential_preview, filter, replacement_id, trace, verification_method, auth_token=args.auth_token, url=args.url)
        elif action == '7':
            credential_data_path = input("Enter path to credential data JSON file: ")
            issue_credential(credential_data_path, auth_token=args.auth_token, url=args.url)
        elif action == '8':
            query_active_connections(auth_token=args.auth_token, url=args.url)
        elif action == '9':
            connection_id = input("Enter connection ID to query messages: ")
            state = input("Enter message state (sent/received): ")
            query_messages(connection_id, state, auth_token=args.auth_token, url=args.url)
        elif action == '10':
            connection_id = input("Enter connection ID to send message: ")
            content = input("Enter message content: ")
            send_message(connection_id, content, auth_token=args.auth_token, url=args.url)
        elif action == '11':
            check_status(auth_token=args.auth_token, url=args.url)
        else:
            print("Invalid action. Please choose 'create-schema', 'get-schema', 'get-cred-def', 'create-cred-def', 'create-invitation', 'send-proposal', 'issue-credential', 'query-connections', 'query-messages', 'send-message', or 'check-status'.")
    elif args.action == 'create-schema':
        create_schema(args.schema_name, args.schema_version, args.attributes, auth_token=args.auth_token, url=args.url)
    elif args.action == 'get-schema':
        get_schema(args.schema_id, auth_token=args.auth_token, url=args.url)
    elif args.action == 'get-cred-def':
        get_credential_definition(args.credential_definition_id, auth_token=args.auth_token, url=args.url)
    elif args.action == 'create-cred-def':
        create_credential_definition(args.schema_id, args.tag, args.support_revocation, auth_token=args.auth_token, url=args.url)
    elif args.action == 'create-invitation':
        create_invitation(args.alias, args.auto_accept, args.public, args.multi_use, auth_token=args.auth_token, url=args.url)
    elif args.action == 'send-proposal':
        send_proposal(args.auto_remove, args.comment, args.connection_id, args.credential_preview, args.filter, args.replacement_id, args.trace, args.verification_method, auth_token=args.auth_token, url=args.url)
    elif args.action == 'issue-credential':
        issue_credential(args.credential_data_path, auth_token=args.auth_token, url=args.url)
    elif args.action == 'query-connections':
        query_active_connections(auth_token=args.auth_token, url=args.url)
    elif args.action == 'query-messages':
        query_messages(args.connection_id, args.state, auth_token=args.auth_token, url=args.url)
    elif args.action == 'send-message':
        send_message(args.connection_id, args.content, auth_token=args.auth_token, url=args.url)
    elif args.action == 'check-status':
        check_status(auth_token=args.auth_token, url=args.url)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

# Create a schema
# python aatp.py create-schema --schema-name "agri_producer" --schema-version "2.0" --attributes "producer_name" "producer_id" "location" "certification_status" "contact_info"
# Get a schema
# python aatp.py get-schema --schema-id "WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0"
# Get a credential definition
# python aatp.py get-cred-def --credential-definition-id "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag"
# Create a credential definition
# python aatp.py create-cred-def --schema-id "VDbghfvE6dGvgA5dK9p1DC:2:agri_producer:1.0" --tag "AgriProducer4"
# Create an invitation
# python aatp.py create-invitation --alias "AgriProducer20" --multi-use
# Send a proposal
# python aatp.py send-proposal --auto-remove --comment "Proposing a membership credential" --connection-id "3fa85f64-5717-4562-b3fc-2c963f66afa6" --credential-preview '{"@type": "issue-credential/2.0/credential-preview", "attributes": [{"mime-type": "image/jpeg", "name": "favourite_drink", "value": "martini"}]}' --filter '{"indy": {"cred_def_id": "WgWxqztrNooG92RXvxSTWv:3:CL:20:tag", "issuer_did": "WgWxqztrNooG92RXvxSTWv", "schema_id": "WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0", "schema_issuer_did": "WgWxqztrNooG92RXvxSTWv", "schema_name": "preferences", "schema_version": "1.0"}}' --replacement-id "3fa85f64-5717-4562-b3fc-2c963f66afa6" --trace --verification-method "string"
# Request a W3C credential
# python aatp.py issue-credential --credential-data-path "path/to/credential_data.json"
# Query active connections
# python aatp.py query-connections
# Query messages
# python aatp.py query-messages --connection-id "b8cfe9d0-9a77-4974-bd1c-45ef83025dae" --state "sent"
# Send a message
# python aatp.py send-message --connection-id "32c6250b-a605-4313-8cb6-827e15b85151" --content "Hello"
# Check status
# python aatp.py check-status
# Interactive mode
# python aatp.py --interactive
