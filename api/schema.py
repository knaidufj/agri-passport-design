import json

from curl import send_api_call
from config import AUTH_TOKEN, API_URL


def create_schema(
    schema_name, schema_version, attributes, auth_token=AUTH_TOKEN, url=API_URL
):
    """
    Create a new schema in the API.

    This function sends a POST request to the API to create a new schema with the specified
    name, version, and attributes. It requires an authorization token and the API URL.

    Args:
        schema_name (str): The name of the schema to be created.
        schema_version (str): The version of the schema to be created.
        attributes (list): A list of attributes that the schema will contain.
        auth_token (str, optional): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str, optional): The API URL for the schema service. Defaults to API_URL.

    Returns:
        dict: The JSON response from the API call containing the created schema details.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    data = {
        "schema_name": schema_name,
        "schema_version": schema_version,
        "attributes": attributes,
    }

    try:
        response = send_api_call(
            f"{url}/schemas", method="POST", headers=headers, data=data
        )
        print("Schema created:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error creating schema: {e}")


def get_schema(schema_id, auth_token=AUTH_TOKEN, url=API_URL):
    """
    Retrieve a schema from the API.

    This function sends a GET request to the API to retrieve the details of a schema
    identified by its schema ID. It requires an authorization token and the API URL.

    Args:
        schema_id (str): The ID of the schema to be retrieved.
        auth_token (str, optional): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str, optional): The API URL for the schema service. Defaults to API_URL.

    Returns:
        dict: The JSON response from the API call containing the schema details.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {"Authorization": f"Bearer {auth_token}", "accept": "application/json"}

    try:
        response = send_api_call(
            f"{url}/schemas/{schema_id}", method="GET", headers=headers
        )
        print("Schema retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error retrieving schema: {e}")


def interactive_create_schema():
    """
    Interactively create a schema.

    This function prompts the user for the schema name, version, and attributes,
    then calls the create_schema function to create the schema.

    It collects input from the user and formats the attributes as a list.
    """
    schema_name = input("Enter schema name: ")
    schema_version = input("Enter schema version: ")
    attributes = input("Enter attributes (comma-separated): ").split(",")
    attributes = [attr.strip() for attr in attributes]
    create_schema(schema_name, schema_version, attributes)


def interactive_get_schema():
    """
    Interactively retrieve a schema.

    This function prompts the user for the schema ID and calls the get_schema function
    to retrieve the schema details.
    """
    schema_id = input("Enter schema ID to retrieve: ")
    get_schema(schema_id)
