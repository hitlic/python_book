import http.client

client = http.client.HTTPConnection("127.0.0.1:9000")
client.request("GET", '/')
resp = client.getresponse()
content = resp.read().decode("utf-8")
client.close()
print(content)
