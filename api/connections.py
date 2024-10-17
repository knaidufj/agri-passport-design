import json
import qrcode

from curl import send_api_call
from config import AUTH_TOKEN, API_URL


def create_invitation(
    alias,
    auto_accept=True,
    public=False,
    multi_use=True,
    auth_token=AUTH_TOKEN,
    url=API_URL,
):
    """
    Create a connection invitation.

    This function sends a request to create a connection invitation with the specified parameters.
    It generates a QR code for the invitation URL and displays it in the terminal.

    Args:
        alias (str): The alias for the invitation.
        auto_accept (bool): Whether to automatically accept the connection. Defaults to True.
        public (bool): Whether the invitation is public. Defaults to False.
        multi_use (bool): Whether the invitation can be used multiple times. Defaults to True.
        auth_token (str): The authorization token for the API call. Defaults to the value in config.
        url (str): The API URL for the connection service. Defaults to the value in config.

    Returns:
        dict: The response from the API call containing the invitation details.

    Raises:
        Exception: If there is an error during the API call or QR code generation.
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    data = {"alias": alias, "auto_accept": auto_accept, "public": public}

    try:
        response = send_api_call(
            f"{url}/connections/create-invitation?multi_use={str(multi_use).lower()}",
            method="POST",
            headers=headers,
            data=data,
        )
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
        img = qr_code.make_image(fill="black", back_color="white")

        # Display the QR code image in the terminal
        img.show()

        return response
    except Exception as e:
        print(f"Error creating connection invitation: {e}")


def query_active_connections(auth_token=AUTH_TOKEN, url=API_URL):
    """
    Query active connections.

    This function sends a request to retrieve the list of active connections.

    Args:
        auth_token (str): The authorization token for the API call. Defaults to the value in config.
        url (str): The API URL for the connection service. Defaults to the value in config.

    Returns:
        dict: The response from the API call containing the active connections.

    Raises:
        Exception: If there is an error during the API call.
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    try:
        response = send_api_call(f"{url}/connections", method="GET", headers=headers)
        print("Active connections:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error querying active connections: {e}")


def interactive_create_invitation():
    """
    Interactively create a connection invitation.

    This function prompts the user for the necessary details to create a connection invitation
    and calls the create_invitation function with the provided inputs.
    """
    alias = input("Enter alias for the invitation: ")
    auto_accept = input("Auto accept connection? (true/false): ").lower() == "true"
    public = input("Make invitation public? (true/false): ").lower() == "true"
    multi_use = (
        input("Allow multiple use of invitation? (true/false): ").lower() == "true"
    )
    create_invitation(alias, auto_accept, public, multi_use)


def interactive_query_connections():
    """
    Interactively query active connections.

    This function calls the query_active_connections function to display the current active connections.
    """
    query_active_connections()
