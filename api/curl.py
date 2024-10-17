import requests
import json

from config import AUTH_TOKEN, API_URL

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