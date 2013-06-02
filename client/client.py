import json
import requests
import examples

data = {'message':'hello world!', 'test':123.4}
url = 'http://localhost:12345/'
headers = {'content-type': 'application/json'}
sheet = examples.example2_formats_simple()
response = requests.post(url, data=json.dumps(sheet), headers=headers)

print(response.text)