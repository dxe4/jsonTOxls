import sys
import json
import requests

from examples import example_functions
import xls_process

example = "4" if len(sys.argv) == 1 else sys.argv[1]
data = example_functions.functions[example]
data["filename"] = "example" + example + ".xls"


def run_without_server():
    xls_process.XlsFactory.create(data)


def run_with_server():
    url = 'http://localhost:12345/'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response)


run_with_server()