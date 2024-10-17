import json

from curl import send_api_call
from config import AUTH_TOKEN, API_URL

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

def interactive_create_schema():
    schema_name = input("Enter schema name: ")
    schema_version = input("Enter schema version: ")
    attributes = input("Enter attributes (comma-separated): ").split(',')
    attributes = [attr.strip() for attr in attributes]
    create_schema(schema_name, schema_version, attributes)

def interactive_get_schema():
    schema_id = input("Enter schema ID to retrieve: ")
    get_schema(schema_id)