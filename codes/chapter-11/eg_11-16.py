from socketserver import ThreadingTCPServer, StreamRequestHandler
from httplib import Parser
from websocketlib import WSParser, WSBuilder, hand_shake


class TCPHandler(StreamRequestHandler):
    def __init__(self, *args, **kwargs):
        self.http_parser = Parser()                    # HTTP解析器
        self.ws_parser = WSParser()                    # WebSocket解析器
        self.ws_builder = WSBuilder()                  # WebSocket构造器
        super().__init__(*args, **kwargs)

    def handle(self):
        hand_shake(self.request, self.http_parser)     # 握手
        self.ws_parser.init(self.request)
        self.ws_builder.init(self.request)
        i = 1
        while True:
            self.ws_parser.parse()                     # 接收并解析WS消息
            print(f'接收到客户端消息：{self.ws_parser.data}')
            send_data = f'msg-第{i:>2}次交互'
            send_data = send_data.encode('utf-8')
            self.ws_builder.build(text_data=send_data)  # 发送第一条消息
            send_data = f'msg-服务器收到：{self.ws_parser.data}'
            if self.ws_parser.data == '':
                send_data = '服务器收到空消息，连接关闭！'
            send_data = send_data.encode('utf-8')
            self.ws_builder.build(text_data=send_data)  # 发送第二条消息
            if self.ws_parser.data == '':
                break
            i += 1


if __name__ == '__main__':
    addr = ('127.0.0.1', 9000)
    with ThreadingTCPServer(addr, TCPHandler) as server:
        server.allow_reuse_address = True
        print(f'WebSocket服务器启动: ws://{addr[0]}:{addr[1]}')
        server.serve_forever()
