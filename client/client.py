import json
import requests
from examples import example_functions


url = 'http://localhost:12345/'
headers = {'content-type': 'application/json'}

example = "4"
data =  example_functions.functions[example]
data["filename"] = "example"+example+".xls"
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)