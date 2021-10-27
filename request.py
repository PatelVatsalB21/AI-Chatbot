import requests
import json
url = 'https://ai-chatbot-2120.herokuapp.com/' # change to your url

# sample data
data = {"msg": "What is computer?"}
data = json.dumps(data)

send_request = requests.post(url, data)
print(send_request.json())
