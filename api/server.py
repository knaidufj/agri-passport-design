from curl import send_api_call
import json
from config import AUTH_TOKEN, API_URL

def check_status(auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "accept": "application/json"
    }
    
    try:
        response = send_api_call(f"{url}/status/ready", method='GET', headers=headers)
        print("Status checked:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error checking status: {e}")

def interactive_check_status():
    check_status()