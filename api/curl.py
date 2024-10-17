import requests
import json

from config import AUTH_TOKEN, API_URL


def send_api_call(url, method="GET", headers=None, data=None):
    """
    Send an API call using the specified HTTP method to the given URL.

    This function constructs a curl command for the API call, prints it for debugging purposes,
    and then executes the request using the requests library. It handles HTTP errors and returns
    the JSON response from the API.

    Args:
        url (str): The URL to which the API call is made.
        method (str): The HTTP method to use for the request (default is "GET").
        headers (dict, optional): A dictionary of HTTP headers to include in the request.
        data (dict, optional): A dictionary of data to send in the body of the request.

    Returns:
        dict: The JSON response from the API if the request is successful.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
    """
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
