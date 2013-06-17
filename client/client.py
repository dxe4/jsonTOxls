import json
import requests
from examples import example_functions

#change to 1,2,3,4 for different examples
example = "4"

url = 'http://localhost:12345/'
headers = {'content-type': 'application/json'}

data =  example_functions.functions[example]
data["filename"] = "example"+example+".xls"
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)