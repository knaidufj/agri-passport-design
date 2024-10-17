import json

from curl import send_api_call
from config import AUTH_TOKEN, API_URL

def send_message(connection_id, content, auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    data = {
        "content": content
    }
    
    try:
        response = send_api_call(f"{url}/connections/{connection_id}/send-message", method='POST', headers=headers, data=data)
        print("Message sent:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error sending message: {e}")

def query_messages(connection_id, state='sent', auth_token=AUTH_TOKEN, url=API_URL):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "accept": "application/json"
    }
    
    try:
        response = send_api_call(f"{url}/basicmessages?connection_id={connection_id}&state={state}", method='GET', headers=headers)
        print("Messages retrieved:\n", json.dumps(response, indent=4))
        return response
    except Exception as e:
        print(f"Error querying messages: {e}")

def interactive_send_message():
    connection_id = input("Enter connection ID to send message: ")
    content = input("Enter message content: ")
    send_message(connection_id, content)

def interactive_query_messages():
    connection_id = input("Enter connection ID to query messages: ")
    state = input("Enter message state (sent/received): ")
    query_messages(connection_id, state)
