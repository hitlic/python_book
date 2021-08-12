import http.client
from urllib.parse import urlencode
client = http.client.HTTPConnection("127.0.0.1:9000")
post_data = {
    "usertag": "test",
    "password": '123456',
    'code': "print('Hello Web')"
}
head_dict = {'Content-Type': 'application/x-www-form-urlencoded'}
post_data = urlencode(post_data)
client.request(method="POST", url='/',
               body=post_data.encode('utf-8'),
               headers=head_dict)
resp = client.getresponse()
content = resp.read().decode("utf-8")
client.close()
print(content)
