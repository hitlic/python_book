import requests
from urllib.parse import urlencode

resp = requests.get("http://127.0.0.1:9000/")           # GET请求
print(resp.text)

post_data = {"usertag": "test",
             "password": "123456",
             "code": "print('Hello Web')"}
head = {'Content-Type': 'application/x-www-form-urlencoded'}
resp = requests.post("http://127.0.0.1:9000/",          # POST请求
                     data=urlencode(post_data), headers=head)
print(resp.text)
