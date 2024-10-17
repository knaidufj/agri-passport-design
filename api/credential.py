import json

from curl import send_api_call
from config import AUTH_TOKEN, API_URL


def get_credential_definition(
    credential_definition_id, auth_token=AUTH_TOKEN, url=API_URL
):
    """
    Retrieve a credential definition from the API.

    This function sends a GET request to the API to retrieve the credential definition
    associated with the provided credential_definition_id. It requires an authorization
    token and the API URL, which default to the values defined in the config.

    Args:
        credential_definition_id (str): The ID of the credential definition to retrieve.
        auth_token (str): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str): The API URL for the credential definitions service. Defaults to API_URL.

    Returns:
        dict: The response from the API containing the credential definition details.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {"Authorization": f"Bearer {auth_token}", "accept": "application/json"}

    try:
        response = send_api_call(
            f"{url}/credential-definitions/{credential_definition_id}",
            method="GET",
            headers=headers,
        )
        print("Credential definition retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error retrieving credential definition: {e}")


def create_credential_definition(
    schema_id, tag, support_revocation=False, auth_token=AUTH_TOKEN, url=API_URL
):
    """
    Create a new credential definition in the API.

    This function sends a POST request to the API to create a new credential definition
    based on the provided schema ID, tag, and revocation support option. It requires
    an authorization token and the API URL, which default to the values defined in the config.

    Args:
        schema_id (str): The ID of the schema to associate with the credential definition.
        tag (str): A tag for the credential definition.
        support_revocation (bool): Indicates if revocation is supported. Defaults to False.
        auth_token (str): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str): The API URL for the credential definitions service. Defaults to API_URL.

    Returns:
        dict: The response from the API containing the created credential definition details.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    data = {
        "schema_id": schema_id,
        "tag": tag,
        "support_revocation": support_revocation,
    }

    try:
        response = send_api_call(
            f"{url}/credential-definitions", method="POST", headers=headers, data=data
        )
        print("Credential definition created:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error creating credential definition: {e}")


def issue_credential(credential_data_json, auth_token=AUTH_TOKEN, url=API_URL):
    """
    Issue a W3C credential.

    This function sends a POST request to the API to issue a W3C credential based on
    the provided credential data in JSON format. It requires an authorization token
    and the API URL, which default to the values defined in the config.

    Args:
        credential_data_json (str): A JSON string containing the credential data.
        auth_token (str): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str): The API URL for issuing credentials. Defaults to API_URL.

    Returns:
        dict: The response from the API containing the issued credential details.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    try:
        credential_data = json.loads(credential_data_json)

        response = send_api_call(
            f"{url}/issue-credential-2.0/send",
            method="POST",
            headers=headers,
            data=credential_data,
        )
        print("W3C Credential requested:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error requesting W3C credential: {e}")


def fetch_credential_records(connection_id, auth_token=AUTH_TOKEN, url=API_URL):
    """
    Fetch credential records associated with a connection ID.

    This function sends a GET request to the API to retrieve credential records
    associated with the specified connection ID. It requires an authorization token
    and the API URL, which default to the values defined in the config.

    Args:
        connection_id (str): The ID of the connection to fetch credential records for.
        auth_token (str): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str): The API URL for fetching credential records. Defaults to API_URL.

    Returns:
        dict: The response from the API containing the credential records.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {"Authorization": f"Bearer {auth_token}", "accept": "application/json"}

    try:
        response = send_api_call(
            f"{url}/issue-credential-2.0/records?connection_id={connection_id}",
            method="GET",
            headers=headers,
        )
        print("Credential records retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error retrieving credential records: {e}")


def interactive_fetch_credential_records():
    """
    Interactively fetch credential records.

    This function prompts the user for a connection ID and calls the
    fetch_credential_records function to retrieve and display the records.
    """
    connection_id = input("Enter connection ID to fetch credential records: ")
    fetch_credential_records(connection_id)


def interactive_issue_credential():
    """
    Interactively issue a W3C credential.

    This function prompts the user for the path to a credential data file,
    reads the file, and calls the issue_credential function to issue the credential.
    """
    credential_data_path = input("Enter path to credential data file: ")

    with open(credential_data_path, "r") as file:
        credential_data_json = file.read()

    issue_credential(credential_data_json)


def send_proposal(
    auto_remove,
    comment,
    connection_id,
    credential_preview,
    filter,
    replacement_id,
    trace,
    verification_method,
    auth_token=AUTH_TOKEN,
    url=API_URL,
):
    """
    Send a credential proposal to a connection.

    This function sends a POST request to the API to propose a credential to a
    specified connection. It requires various parameters including the connection ID,
    credential preview, and other options. It also requires an authorization token
    and the API URL, which default to the values defined in the config.

    Args:
        auto_remove (bool): Indicates if the proposal should be automatically removed.
        comment (str): A comment to include with the proposal.
        connection_id (str): The ID of the connection to send the proposal to.
        credential_preview (dict): A preview of the credential being proposed.
        filter (dict): A filter to apply to the proposal.
        replacement_id (str): The ID of a credential proposal to replace, if any.
        trace (bool): Indicates if tracing should be enabled for the proposal.
        verification_method (str): The verification method to use for the proposal.
        auth_token (str): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str): The API URL for sending proposals. Defaults to API_URL.

    Returns:
        dict: The response from the API containing the result of the proposal.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    data = {
        "auto_remove": auto_remove,
        "comment": comment,
        "connection_id": connection_id,
        "credential_preview": credential_preview,
        "filter": filter,
        "replacement_id": replacement_id,
        "trace": trace,
        "verification_method": verification_method,
    }

    try:
        response = send_api_call(
            f"{url}/issue-credential-2.0/send-proposal",
            method="POST",
            headers=headers,
            data=data,
        )
        print("Proposal sent:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error sending proposal: {e}")


def interactive_get_credential_definition():
    """
    Interactively retrieve a credential definition.

    This function prompts the user for a credential definition ID and calls the
    get_credential_definition function to retrieve and display the definition.
    """
    credential_definition_id = input("Enter credential definition ID to retrieve: ")
    get_credential_definition(credential_definition_id)


def interactive_create_credential_definition():
    """
    Interactively create a new credential definition.

    This function prompts the user for the schema ID, tag, and revocation support option,
    and calls the create_credential_definition function to create the new definition.
    """
    schema_id = input("Enter schema ID: ")
    tag = input("Enter tag for credential definition: ")
    support_revocation = input("Support revocation? (true/false): ").lower() == "true"
    create_credential_definition(schema_id, tag, support_revocation)


def interactive_send_proposal():
    """
    Interactively send a credential proposal.

    This function prompts the user for various parameters required to send a credential
    proposal and calls the send_proposal function to execute the action.
    """
    auto_remove = input("Auto remove? (true/false): ").lower() == "true"
    comment = input("Enter comment for the proposal: ")
    connection_id = input("Enter connection ID: ")
    credential_preview = json.loads(input("Enter credential preview as JSON: "))
    filter = json.loads(input("Enter filter as JSON: "))
    replacement_id = input("Enter replacement ID: ")
    trace = input("Enable trace? (true/false): ").lower() == "true"
    verification_method = input("Enter verification method: ")
    send_proposal(
        auto_remove,
        comment,
        connection_id,
        credential_preview,
        filter,
        replacement_id,
        trace,
        verification_method,
    )
