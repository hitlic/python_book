from socket import socket, AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
from datetime import datetime
import asyncio


async def service_task(conn, addr, loop):
    print(f'客户端{addr}连接成功，等待输入 ...')
    while True:                                           # 通信循环
        data_recv = (await loop.sock_recv(conn, 1024))    # 异步接收数据
        data_recv = data_recv.decode('utf-8')
        now = datetime.now().strftime("%H:%M:%S")
        print(f'{now} 接收到来自{addr}的数据：{data_recv}')
        send_data = f'接收到长度为 {len(data_recv)} 的数据'
        send_data = send_data.encode('utf-8')
        await loop.sock_sendall(conn, send_data)          # 异步发送数据
        if not data_recv:
            conn.close()
            break
    print(f'客户端{addr}连接结束！')


async def server_routine(server_socket, loop):
    while True:
        conn, addr = await loop.sock_accept(server_socket)  # 异步接受连接
        loop.create_task(service_task(conn, addr, loop))


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)        # 创建套接字
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # 端口重用
    server_socket.bind(('127.0.0.1', 9000))               # 绑定地址
    server_socket.listen()
    print('TCP服务器启动，监听之中... ...')
    server_socket.setblocking(False)  # 设置为非阻塞套接字
    loop = asyncio.get_event_loop()
    routine = server_routine(server_socket, loop)
    loop.run_until_complete(routine)
    loop.close()


if __name__ == '__main__':
    main()
