
import axios from 'axios' 

let session_id;

const chatSession = await axios.post(
   'https://agentivehub.com/api/chat/session',
 {
    "api_key": "e06a7619-6d0a-4b76-b89a-072883c52399",
     "assistant_id": "69a36854-f322-49de-ba11-4aafd9b65761",
    }
)

session_id = chatSession.data.session_id;

const chatReponse = {
 api_key: "e06a7619-6d0a-4b76-b89a-072883c52399",
 session_id,
 type: 'custom_code',
 assistant_id: "69a36854-f322-49de-ba11-4aafd9b65761",
 messages:[{ role: 'user',  content: 'Say Hello!' }],
 };

const chat = await axios.post(
   'https://agentivehub.com/api/chat',
 chatReponse
 );
  return chat.data;
    
