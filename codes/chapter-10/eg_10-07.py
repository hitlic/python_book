from socket import socket, AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
from datetime import datetime
from multiprocessing import Process


class ServiceProcess(Process):
    def __init__(self, socket, addr):
        self.conn = socket
        self.addr = addr
        super().__init__()

    def run(self):
        print(f'客户端{self.addr}连接成功，等待输入 ...')
        while True:                                       # 通信循环
            data_recv = self.conn.recv(1024)              # 接收数据
            data_recv = data_recv.decode('utf-8')
            now = datetime.now().strftime("%H:%M:%S")
            print(f'{now} 接收到来自{self.addr}的数据：{data_recv}')
            send_data = f'接收到长度为 {len(data_recv)} 的数据'
            self.conn.send(send_data.encode('utf-8'))     # 发送数据
            if not data_recv:
                self.conn.close()
                break
        print(f'客户端{self.addr}连接结束！')


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)        # 创建套接字对象
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
    server_socket.bind(('127.0.0.1', 9000))               # 绑定地址
    server_socket.listen()                                # 监听
    print('TCP服务器启动，监听之中... ...')
    while True:
        conn_socket, addr = server_socket.accept()        # 接受连接请求
        subp = ServiceProcess(conn_socket, addr)          # 创建子进程
        subp.start()                                      # 启动子进程


if __name__ == '__main__':
    main()
