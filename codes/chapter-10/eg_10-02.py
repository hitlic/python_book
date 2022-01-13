from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime

tcp_socket = socket(AF_INET, SOCK_STREAM)    # 创建套接字
tcp_socket.connect(('127.0.0.1', 9000))               # 发起连接请求
while True:
    data_send = input('> ')
    tcp_socket.send(data_send.encode('utf-8'))        # 发送数据
    if not data_send:
        break
    data_recv = tcp_socket.recv(1024)                 # 接收数据
    now = datetime.now().strftime("%H:%M:%S")
    print(f'{now} 服务器回复：{data_recv.decode("utf-8")}')
tcp_socket.close()
