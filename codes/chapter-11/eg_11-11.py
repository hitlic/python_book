from urllib.parse import urlencode
from urllib import request

resp = request.urlopen("http://127.0.0.1:9000/")        # GET 请求
content = resp.read().decode("utf-8")
print(content)

post_data = {"usertag": "test",
             "password": "123456",
             "code": "print('Hello Web')"}
head = {'Content-Type': 'application/x-www-form-urlencoded'}
req = request.Request("http://127.0.0.1:9000/",         # POST请求
                      data=urlencode(post_data).encode('utf-8'),
                      headers=head, method='POST')
resp = request.urlopen(req)
content = resp.read().decode("utf-8")
print(content)
