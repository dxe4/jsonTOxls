import socket
import json
import requests

data = {'message':'hello world!', 'test':123.4}

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 8082))#13373
# s.send(bytes(json.dumps(data), 'UTF-8'))
# result = json.loads(s.recv(1024).decode('UTF-8'))
# print(result)
# s.close()

url = 'http://localhost:12345/'
#payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
sheet1 = {
        'A1': 'Item',#{'value':'Item'},
        'B1':'Cost',
         #
        'A2':'Rent',
        'A3':'Gas',
        'A4':'Food',
        'A5':'Gym',
        'A6':'Total',
         #
        'B2':'1000',
        'B3':'100',
        'B4':'300',
        'B5':'50',
        'B6':'=SUM(B1:B4)'
    }

sheet = [{"Test Sheet" :  sheet1}]

response = requests.post(url, data=json.dumps(sheet), headers=headers)

print(response.text)