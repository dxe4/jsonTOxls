import sys,os,imp
import json
import requests
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
class_path = imp.load_source('module.name', project_dir+'/common/class_path.py')
class_path.append_path()

from examples import example_functions

#change to 1,2,3,4 for different examples
example = "4" if  len(sys.argv) == 1 else sys.argv[1]

url = 'http://localhost:12345/'
headers = {'content-type': 'application/json'}

data =  example_functions.functions[example]
data["filename"] = "example"+example+".xls"
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)