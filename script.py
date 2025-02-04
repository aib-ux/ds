
import requests
api_key = "e06a7619-6d0a-4b76-b89a-072883c52399"

chat_session = requests.post(
    'https://agentivehub.com/api/chat/session',
    json = {
        "api_key" : "api_key",
        "assistant_id" : "69a36854-f322-49de-ba11-4aafd9b65761",    
    }
)

# Get the chat session ID
chat_session_id = chat_session.json()["session_id"]
   
# Send a message to the chat session
chat_response = {
    "api_key" : api_key,
    "session_id" : chat_session_id,
    "type" : "custom_code",
    "assistant_id" : "69a36854-f322-49de-ba11-4aafd9b65761",
    "messages" : [{"role": "user", "content": "Say Hello!"}]
}

req = requests.post(
    'https://agentivehub.com/api/chat',
    json = chat_response
)
resp = req.json()
