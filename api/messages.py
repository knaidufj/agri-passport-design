import json

from curl import send_api_call
from config import AUTH_TOKEN, API_URL


def send_message(connection_id, content, auth_token=AUTH_TOKEN, url=API_URL):
    """
    Send a message to a specific connection.

    This function constructs a POST request to send a message to the specified connection
    using the provided content. It requires the connection ID and can optionally take an
    authorization token and API URL.

    Args:
        connection_id (str): The ID of the connection to which the message will be sent.
        content (str): The content of the message to be sent.
        auth_token (str, optional): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str, optional): The API URL for the message service. Defaults to API_URL.

    Returns:
        dict: The JSON response from the API call if the message is sent successfully.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "accept": "application/json",
    }
    data = {"content": content}

    try:
        response = send_api_call(
            f"{url}/connections/{connection_id}/send-message",
            method="POST",
            headers=headers,
            data=data,
        )
        print("Message sent:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error sending message: {e}")


def query_messages(connection_id, state="sent", auth_token=AUTH_TOKEN, url=API_URL):
    """
    Query messages for a specific connection.

    This function sends a GET request to retrieve messages associated with a given connection ID.
    It allows filtering messages by their state (sent or received).

    Args:
        connection_id (str): The ID of the connection for which messages are queried.
        state (str, optional): The state of messages to query (sent or received). Defaults to "sent".
        auth_token (str, optional): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str, optional): The API URL for the message service. Defaults to API_URL.

    Returns:
        dict: The JSON response from the API call containing the queried messages.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {"Authorization": f"Bearer {auth_token}", "accept": "application/json"}

    try:
        response = send_api_call(
            f"{url}/basicmessages?connection_id={connection_id}&state={state}",
            method="GET",
            headers=headers,
        )
        print("Messages retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error querying messages: {e}")


def interactive_send_message():
    """
    Interactively send a message to a specific connection.

    This function prompts the user for the connection ID and message content, then calls
    the send_message function to send the message.
    """
    connection_id = input("Enter connection ID to send message: ")
    content = input("Enter message content: ")
    send_message(connection_id, content)


def interactive_query_messages():
    """
    Interactively query messages for a specific connection.

    This function prompts the user for the connection ID and message state, then calls
    the query_messages function to retrieve the messages.
    """
    connection_id = input("Enter connection ID to query messages: ")
    state = input("Enter message state (sent/received): ")
    query_messages(connection_id, state)
