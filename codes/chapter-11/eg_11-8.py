import socket
from urllib.parse import quote
from httplib import Parser

client_socket = socket.socket()
addr = ('127.0.0.1', 9000)
client_socket.connect(addr)
# 请求正文
code = '''print("Hello Web")'''
request_content = f'usertag=test&password=123456&code={quote(code)}'
# 请求头
request = ['POST / HTTP/1.1\r\n',
           f'Content-Length: {len(request_content)}\r\n',
           'Content-Type: application/x-www-form-urlencoded\r\n\r\n',
           request_content]
client_socket.send(''.join(request).encode('utf-8'))             # 发送请求
parser = Parser()
while True:                                             # 通信循环
    resp = client_socket.recv(1024)
    parser.append(resp)
    if parser.is_ok():
        break
client_socket.close()
print(parser.content())