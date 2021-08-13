from socketserver import ThreadingTCPServer, StreamRequestHandler
from httplib import Parser

class TCPHandler(StreamRequestHandler):
    def __init__(self, *args, **kwargs):
        self.parser = Parser()
        super().__init__(*args, **kwargs)

    def handle(self):
        while True:                               # 通信循环
            data_recv = self.request.recv(1024)   # 接收数据
            self.parser.append(data_recv)
            if self.parser.is_ok():
                break
        print(f'{self.client_address} {self.parser.req_method} 请求')
        if self.parser.req_method == 'GET':
            send_data = self.do_GET()             # 处理GET请求
        elif self.parser.req_method == 'POST':
            send_data = self.do_POST()            # 处理POST请求
        else:
            send_data = self.do_error()           # 处理错误
        self.request.sendall(send_data)           # 发送数据
        self.request.close()

    def do_GET(self):                             # 处理GET请求
        html = self.load_file()
        if html is None:
            return self.do_error()
        else:
            body = html.encode('utf8')
            head = self.make_head('200', len(body))
            return head + body

    def do_POST(self):                            # 处理POST请求
        html = self.load_file()
        if html is None:
            return self.do_error()
        else:
            info = f'你的请求参数是：{self.parser.req_params()}'
            html = html.replace('<span id="info"/>', info)
            body = html.encode('utf8')
            head = self.make_head('200', len(body))
            return head + body

    def make_head(self, code, content_len):       # 生成响应头
        head = b''
        if code == '200':
            head += b'HTTP/1.1 200 OK\r\n'
        elif code == '404':
            head += b'HTTP/1.1 404 Not Found\r\n'
        head += f'Content-Length: {content_len}\r\n'.encode('utf-8')
        head += b'Content-Type: text/html; charset=utf-8\r\n\r\n'
        return head

    def load_file(self):                          # 加载文件
        try:
            req_url = self.parser.req_url
            path = '/index.html' if req_url == '/' else req_url
            with open(f'.{path}') as f:
                return f.read()
        except Exception:
            return None

    def do_error(self):                           # 处理错误请求
        return self.make_head('404', 18) + '404页面不存在'.encode('utf-8')

if __name__ == '__main__':
    addr = ('127.0.0.1', 9000)
    with ThreadingTCPServer(addr, TCPHandler) as server:
        server.allow_reuse_address = True
        print(f'HTTP服务器启动: http://{addr[0]}:{addr[1]}')
        server.serve_forever()