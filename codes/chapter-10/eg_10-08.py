from socket import socket, AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor


def service_task(conn, addr):
    print(f'客户端{addr}连接成功，等待输入 ...')
    while True:                                           # 通信循环
        data_recv = conn.recv(1024).decode('utf-8')       # 接收数据
        now = datetime.now().strftime("%H:%M:%S")
        print(f'{now} 接收到来自{addr}的数据：{data_recv}')
        send_data = f'接收到长度为 {len(data_recv)} 的数据'
        conn.send(send_data.encode('utf-8'))              # 发送数据
        if not data_recv:
            conn.close()
            break
    print(f'客户端{addr}连接结束！')


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)        # 创建套接字对象
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
    server_socket.bind(('127.0.0.1', 9000))               # 绑定地址
    server_socket.listen()
    print('TCP服务器启动，监听之中... ...')
    pool = ProcessPoolExecutor(10)                        # 进程池
    while True:
        conn, addr = server_socket.accept()               # 接受连接请求
        pool.submit(service_task, conn, addr)


if __name__ == '__main__':
    main()
