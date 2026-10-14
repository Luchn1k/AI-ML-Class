import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer ADD_YOUR_API_KEY",
  },
  data=json.dumps({
    "model": "openrouter/free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)

print(type(response.text))
response_json = json.loads(response.text)
print(type(response_json))
print(response_json['choices'][0]['message']['content'])
