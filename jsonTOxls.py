import sys
import os
import imp
import json
import requests

project_dir = os.path.abspath(os.path.dirname(__file__))
print(project_dir)
class_path = imp.load_source('module.name', project_dir + '/common/class_path.py')
class_path.append_path()

from examples import example_functions
from excel import xlsx_factory

#change to 1,2,3,4 for different examples
example = "4" if len(sys.argv) == 1 else sys.argv[1]
data = example_functions.functions[example]
data["filename"] = "example" + example + ".xls"


def run_without_server():
    xlsx_factory.create(data)


def run_with_server():
    url = 'http://localhost:12345/'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response)

run_without_server()