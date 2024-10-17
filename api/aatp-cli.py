import argparse
import json
import os

from config import AUTH_TOKEN, API_URL
from schema import (
    interactive_create_schema,
    interactive_get_schema,
    get_schema,
    create_schema,
)
from connections import (
    create_invitation,
    query_active_connections,
    interactive_create_invitation,
    interactive_query_connections,
)
from credential import (
    get_credential_definition,
    create_credential_definition,
    issue_credential,
    send_proposal,
    interactive_get_credential_definition,
    interactive_create_credential_definition,
    interactive_issue_credential,
    interactive_send_proposal,
    fetch_credential_records,
    interactive_fetch_credential_records,
)
from messages import (
    send_message,
    query_messages,
    interactive_query_messages,
    interactive_send_message,
)
from server import check_status, interactive_check_status


def main():
    parser = argparse.ArgumentParser(
        description="A command line utility for demonstrating Australian Agricultural Traceability Protocol."
    )

    # Main options
    parser.add_argument(
        "--interactive", action="store_true", help="Run in interactive mode."
    )
    parser.add_argument(
        "--auth-token",
        type=str,
        default=AUTH_TOKEN,
        help="Authorization token for API calls.",
    )
    parser.add_argument(
        "--url", type=str, default=API_URL, help="URL for the API endpoint."
    )

    # Sub-parsers for different actions
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    # Create schema sub-parser
    parser_schema = subparsers.add_parser("create-schema", help="Create a new schema")
    parser_schema.add_argument(
        "--schema-name", type=str, required=True, help="Name of the schema to create."
    )
    parser_schema.add_argument(
        "--schema-version",
        type=str,
        required=True,
        help="Version of the schema to create.",
    )
    parser_schema.add_argument(
        "--attributes",
        type=str,
        nargs="+",
        required=True,
        help="List of attributes for the schema.",
    )

    # Get schema sub-parser
    parser_get_schema = subparsers.add_parser(
        "get-schema", help="Retrieve an existing schema"
    )
    parser_get_schema.add_argument(
        "--schema-id", type=str, required=True, help="ID of the schema to retrieve."
    )

    # Get credential definition sub-parser
    parser_get_cred_def = subparsers.add_parser(
        "get-cred-def", help="Retrieve an existing credential definition"
    )
    parser_get_cred_def.add_argument(
        "--credential-definition-id",
        type=str,
        required=True,
        help="ID of the credential definition to retrieve.",
    )

    # Create credential definition sub-parser
    parser_cred_def = subparsers.add_parser(
        "create-cred-def", help="Create a new credential definition"
    )
    parser_cred_def.add_argument(
        "--schema-id",
        type=str,
        required=True,
        help="Schema ID for creating credential definition.",
    )
    parser_cred_def.add_argument(
        "--tag", type=str, required=True, help="Tag for the credential definition."
    )
    parser_cred_def.add_argument(
        "--support-revocation",
        action="store_true",
        help="Enable support for revocation in credential definition.",
    )

    # Create invitation sub-parser
    parser_invitation = subparsers.add_parser(
        "create-invitation", help="Create a new connection invitation"
    )
    parser_invitation.add_argument(
        "--alias", type=str, required=True, help="Alias for the invitation."
    )
    parser_invitation.add_argument(
        "--auto-accept", action="store_true", help="Auto accept the connection."
    )
    parser_invitation.add_argument(
        "--public", action="store_true", help="Make the invitation public."
    )
    parser_invitation.add_argument(
        "--multi-use", action="store_true", help="Allow multiple use of the invitation."
    )

    # Send proposal sub-parser
    parser_send_proposal = subparsers.add_parser(
        "send-proposal", help="Send a credential proposal"
    )
    parser_send_proposal.add_argument(
        "--auto-remove",
        action="store_true",
        help="Automatically remove the proposal after it is sent.",
    )
    parser_send_proposal.add_argument(
        "--comment", type=str, required=True, help="Comment for the proposal."
    )
    parser_send_proposal.add_argument(
        "--connection-id",
        type=str,
        required=True,
        help="Connection ID for the proposal.",
    )
    parser_send_proposal.add_argument(
        "--credential-preview",
        type=json.loads,
        required=True,
        help="JSON string of the credential preview.",
    )
    parser_send_proposal.add_argument(
        "--filter",
        type=json.loads,
        required=True,
        help="JSON string of the filter for the proposal.",
    )
    parser_send_proposal.add_argument(
        "--replacement-id",
        type=str,
        required=True,
        help="Replacement ID for the proposal.",
    )
    parser_send_proposal.add_argument(
        "--trace", action="store_true", help="Enable tracing for the proposal."
    )
    parser_send_proposal.add_argument(
        "--verification-method",
        type=str,
        required=True,
        help="Verification method for the proposal.",
    )

    # Request W3C credential sub-parser
    parser_request_w3c = subparsers.add_parser(
        "issue-credential", help="Request a W3C credential"
    )
    parser_request_w3c.add_argument(
        "--credential-data",
        type=str,
        required=True,
        help="JSON string containing the credential data.",
    )

    # Fetch credential records sub-parser
    parser_fetch_cred_records = subparsers.add_parser(
        "fetch-cred-records", help="Fetch credential records for a connection"
    )
    parser_fetch_cred_records.add_argument(
        "--connection-id",
        type=str,
        required=True,
        help="Connection ID to fetch credential records for.",
    )

    # Query active connections sub-parser
    parser_connections = subparsers.add_parser(
        "query-connections", help="Query active connections"
    )

    # Query messages sub-parser
    parser_query_messages = subparsers.add_parser(
        "query-messages", help="Query messages for a specific connection"
    )
    parser_query_messages.add_argument(
        "--connection-id",
        type=str,
        required=True,
        help="Connection ID to query messages for.",
    )
    parser_query_messages.add_argument(
        "--state",
        type=str,
        default="sent",
        help="State of messages to query (sent/received).",
    )

    # Send message sub-parser
    parser_send_message = subparsers.add_parser(
        "send-message", help="Send a message to a specific connection"
    )
    parser_send_message.add_argument(
        "--connection-id",
        type=str,
        required=True,
        help="Connection ID to send the message to.",
    )
    parser_send_message.add_argument(
        "--content", type=str, required=True, help="Content of the message to send."
    )

    # Check status sub-parser
    parser_check_status = subparsers.add_parser(
        "check-status", help="Check the status of the service"
    )

    args = parser.parse_args()

    action_map = {
        "1": interactive_create_schema,
        "2": interactive_get_schema,
        "3": interactive_get_credential_definition,
        "4": interactive_create_credential_definition,
        "5": interactive_create_invitation,
        "6": interactive_send_proposal,
        "7": interactive_issue_credential,
        "8": interactive_query_connections,
        "9": interactive_query_messages,
        "10": interactive_send_message,
        "11": interactive_check_status,
        "12": interactive_fetch_credential_records,
    }

    if args.interactive:
        action = input(
            "\nChoose an action:\n"
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
            "12. Fetch Credential Records\n"
            "Please enter the action number: "
        ).lower()

        action_function = action_map.get(action)
        if action_function:
            action_function()
        else:
            print(
                "Invalid action. Please choose 'create-schema', 'get-schema', 'get-cred-def', 'create-cred-def', 'create-invitation', 'send-proposal', 'issue-credential', 'query-connections', 'query-messages', 'send-message', 'check-status', or 'fetch-cred-records'."
            )
    else:
        action_map = {
            "create-schema": lambda: create_schema(
                args.schema_name,
                args.schema_version,
                args.attributes,
                auth_token=args.auth_token,
                url=args.url,
            ),
            "get-schema": lambda: get_schema(
                args.schema_id, auth_token=args.auth_token, url=args.url
            ),
            "get-cred-def": lambda: get_credential_definition(
                args.credential_definition_id, auth_token=args.auth_token, url=args.url
            ),
            "create-cred-def": lambda: create_credential_definition(
                args.schema_id,
                args.tag,
                args.support_revocation,
                auth_token=args.auth_token,
                url=args.url,
            ),
            "create-invitation": lambda: create_invitation(
                args.alias,
                args.auto_accept,
                args.public,
                args.multi_use,
                auth_token=args.auth_token,
                url=args.url,
            ),
            "send-proposal": lambda: send_proposal(
                args.auto_remove,
                args.comment,
                args.connection_id,
                args.credential_preview,
                args.filter,
                args.replacement_id,
                args.trace,
                args.verification_method,
                auth_token=args.auth_token,
                url=args.url,
            ),
            "issue-credential": lambda: issue_credential(
                args.credential_data, auth_token=args.auth_token, url=args.url
            ),
            "fetch-cred-records": lambda: fetch_credential_records(
                args.connection_id, auth_token=args.auth_token, url=args.url
            ),
            "query-connections": lambda: query_active_connections(
                auth_token=args.auth_token, url=args.url
            ),
            "query-messages": lambda: query_messages(
                args.connection_id, args.state, auth_token=args.auth_token, url=args.url
            ),
            "send-message": lambda: send_message(
                args.connection_id,
                args.content,
                auth_token=args.auth_token,
                url=args.url,
            ),
            "check-status": lambda: check_status(
                auth_token=args.auth_token, url=args.url
            ),
        }

        action_function = action_map.get(args.action)
        if action_function:
            action_function()
        else:
            parser.print_help()


if __name__ == "__main__":
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
