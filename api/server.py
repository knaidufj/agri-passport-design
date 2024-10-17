from curl import send_api_call
import json
from config import AUTH_TOKEN, API_URL


def check_status(auth_token=AUTH_TOKEN, url=API_URL):
    """
    Check the status of the service.

    This function sends a GET request to the specified URL to check if the service is ready.
    It requires an authorization token to access the endpoint.

    Args:
        auth_token (str, optional): The authorization token for the API call. Defaults to AUTH_TOKEN.
        url (str, optional): The API URL for the status endpoint. Defaults to API_URL.

    Returns:
        dict: The JSON response from the API call containing the status information.

    Raises:
        Exception: If there is an error during the API call or if the response is not successful.
    """
    headers = {"Authorization": f"Bearer {auth_token}", "accept": "application/json"}

    try:
        response = send_api_call(f"{url}/status/ready", method="GET", headers=headers)
        print("Status checked:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error checking status: {e}")


def interactive_check_status():
    """
    Interactively check the status of the service.

    This function calls the check_status function to retrieve and display the current status
    of the service. It does not require any user input.
    """
    check_status()
