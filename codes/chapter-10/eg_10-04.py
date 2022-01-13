from socket import socket, AF_INET, SOCK_DGRAM
import datetime

client_socket = socket(AF_INET, SOCK_DGRAM)            # 创建套接字
while True:
    data_send = input('> ').encode("utf-8")
    if not data_send:
        break
    client_socket.sendto(data_send, ('127.0.0.1', 9000))  # 发送数据
    data_recv, addr = client_socket.recvfrom(1024)        # 接收数据
    now = datetime.datetime.now().strftime("%H:%M:%S")
    data_recv = data_recv.decode(encoding="utf-8")
    print(f'{now} 服务器回复：{data_recv}')
client_socket.close()
