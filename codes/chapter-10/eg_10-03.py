from socket import socket, AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_REUSEADDR
from datetime import datetime

server_socket = socket(AF_INET, SOCK_DGRAM)              # 创建套接字
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)    # 端口重用
server_socket.bind(('127.0.0.1', 9000))                  # 绑定地址
print('UDP服务器启动，等待客户端数据 ...')

while True:
    data_recv, address = server_socket.recvfrom(1024)    # 接收数据
    now = datetime.now().strftime("%H:%M:%S")
    data_recv = data_recv.decode("utf-8")
    print(f'{now}接收到来自{address[0]}的数据：{data_recv}')
    data_send = f'接收到长度为 {len(data_recv)} 的数据'.encode('utf-8')
    server_socket.sendto(data_send, address)             # 发送数据
server_socket.close()
