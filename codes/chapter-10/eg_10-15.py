from socketserver import ThreadingTCPServer, StreamRequestHandler
from datetime import datetime


class TCPHandler(StreamRequestHandler):                     # 请求处理器
    def handle(self):
        print(f'客户端{self.client_address}连接成功，等待输入 ...')
        while True:                                         # 通信循环
            data_recv = self.request.recv(1024)             # 接收数据
            data_recv = data_recv.decode('utf-8')
            now = datetime.now().strftime("%H:%M:%S")
            print(f'{now} 接收到来自{self.client_address}的数据：{data_recv}')
            send_data = f'接收到长度为 {len(data_recv)} 的数据'
            self.request.send(send_data.encode('utf-8'))    # 发送数据
            if not data_recv:
                break
        print(f'客户端{self.client_address}连接结束！')


if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 9000), TCPHandler) as server:
        print('TCP服务器启动，监听之中... ...')
        server.serve_forever()
