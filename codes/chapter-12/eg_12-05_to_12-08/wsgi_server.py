# 文件 wsgi_server.py
from socket import socket, AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
from httplib import Parser
import threading, sys, io

class WSGIServer:
    def __init__(self, app, host='127.0.0.1', port=9000):
        self.app = app
        self.host = host
        self.port = port
        self.resp_status = None
        self.resp_headers = None

    def start(self):
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        print(f"启动服务器，http://{self.host}:{self.port}")
        server_socket.bind((self.host, self.port))
        server_socket.listen(10)
        while True:                                        # 服务循环
            conn, addr = server_socket.accept()
            try:
                conn.settimeout(60)
                print(f"客户端：{addr}")
                threading.Thread(target=self.server_thread,# 服务线程
                                 args=(conn,)).start()
            except Exception:
                print('服务器发生错误！')

    def start_response(self, status, headers):
        self.resp_status, self.resp_headers = status, headers

    def server_thread(self, conn):
        parser = Parser()
        while True:                                        # 通信循环
            parser.append(conn.recv(1024))
            if parser.is_ok():
                break
        env = self.make_env(parser)                        # 构造环境变量
        app_contents = self.app(env, self.start_response)  # 调用WSGI应用
        resp_text = self.make_head(self.resp_status, self.resp_headers)
        response = resp_text.encode('utf-8')
        response += b' '.join(app_contents)
        conn.send(response)                                # HTTP响应
        conn.close()

    def make_head(self, status, headers):                  # 构造响应头
        head = f'HTTP/1.1 {status}\r\n'
        for k, v in headers:
            head += f'{k}: {v}\r\n'
        head += '\r\n'
        return head

    def make_env(self, parser):                            # 环境变量字典
        return {
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.input': io.BytesIO(parser.body),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': True,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
            'REQUEST_METHOD': parser.req_method,
            'SCRIPT_NAME': '',
            'PATH_INFO': parser.req_url,
            'CONTENT_TYPE': parser.content_type,
            'CONTENT_LENGTH': parser.content_length,
            'SERVER_NAME': self.host,
            'SERVER_PORT': self.port,
            'QUERY_STRING': parser.query_string,
            'SERVER_PROTOCOL': 'HTTP 1.1',
            'HTTP_COOKIE': parser.head_dict.get('cookie', ''),
            'params': parser.req_params()
        }

if __name__ == '__main__':
    from wsgi_apps import first_wsgi_app
    server = WSGIServer(first_wsgi_app)
    server.start()