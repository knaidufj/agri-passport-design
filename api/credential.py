import json

from curl import send_api_call
from config import AUTH_TOKEN, API_URL

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

def create_offer(auto_issue, auto_remove, comment, credential_preview, filter, replacement_id, trace, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data = {
        "auto_issue": auto_issue,
        "auto_remove": auto_remove,
        "comment": comment,
        "credential_preview": credential_preview,
        "filter": filter,
        "replacement_id": replacement_id,
        "trace": trace
    }
    
    try:
        response = send_api_call(f"{url}/issue-credential-2.0/create-offer", method='POST', headers=headers, data=data)
        print("Offer created:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error creating offer: {e}")

def interactive_create_offer():
    auto_issue = input("Auto issue? (true/false): ").lower() == 'true'
    auto_remove = input("Auto remove? (true/false): ").lower() == 'true'
    comment = input("Enter comment for the offer: ")
    credential_preview = json.loads(input("Enter credential preview as JSON: "))
    filter = json.loads(input("Enter filter as JSON: "))
    replacement_id = input("Enter replacement ID: ")
    trace = input("Enable trace? (true/false): ").lower() == 'true'
    create_offer(auto_issue, auto_remove, comment, credential_preview, filter, replacement_id, trace)

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

def interactive_get_credential_definition():
    credential_definition_id = input("Enter credential definition ID to retrieve: ")
    get_credential_definition(credential_definition_id)

def interactive_create_credential_definition():
    schema_id = input("Enter schema ID: ")
    tag = input("Enter tag for credential definition: ")
    support_revocation = input("Support revocation? (true/false): ").lower() == 'true'
    create_credential_definition(schema_id, tag, support_revocation)

def interactive_issue_credential():
    credential_data_path = input("Enter path to credential data file: ")
    issue_credential(credential_data_path)

def interactive_send_proposal():
    auto_remove = input("Auto remove? (true/false): ").lower() == 'true'
    comment = input("Enter comment for the proposal: ")
    connection_id = input("Enter connection ID: ")
    credential_preview = json.loads(input("Enter credential preview as JSON: "))
    filter = json.loads(input("Enter filter as JSON: "))
    replacement_id = input("Enter replacement ID: ")
    trace = input("Enable trace? (true/false): ").lower() == 'true'
    verification_method = input("Enter verification method: ")
    send_proposal(auto_remove, comment, connection_id, credential_preview, filter, replacement_id, trace, verification_method)