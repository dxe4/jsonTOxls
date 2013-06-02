import json
import requests
from examples import examples


url = 'http://localhost:12345/'
headers = {'content-type': 'application/json'}

example = "3"
data =  examples.functions[example]
data["filename"] = "example"+example+".xls"
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)