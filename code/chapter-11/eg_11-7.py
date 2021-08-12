import socket
from httplib import Parser

client_socket = socket.socket()
addr = ('127.0.0.1', 9000)
client_socket.connect(addr)

request = f"GET / HTTP/1.1\r\nHost:{addr[0]}\r\n\r\n"
client_socket.send(request.encode('utf-8'))       # 发出请求

parser = Parser()
while True:                                       # 通信循环
    resp = client_socket.recv(1024)
    parser.append(resp)
    if parser.is_ok():
        break
client_socket.close()
print(parser.content())
