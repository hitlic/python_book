from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):                             # 响应GET请求
        html = self.load_file()
        if html is not None:
            self.make_response(html.encode('utf-8'))
        else:
            self.send_error(404, f'Page not found!')

    def do_POST(self):                            # 响应POST请求
        html = self.load_file()
        if html is not None:
            query = self.rfile.read(int(self.headers['content-length']))
            params = parse_qs(query.decode("utf-8"))
            html = html.replace('<span id="info"/>', str(params))
            self.make_response(html.encode('utf-8'))
        else:
            self.send_error(404, f'Page not found!')

    def load_file(self):                          # 加载文件
        try:
            path = '/index.html' if self.path == '/' else self.path
            with open(f'.{path}') as f:
                return f.read()
        except Exception:
            return None

    def make_response(self, body):                # 构造HTTP响应
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

if __name__ == '__main__':
    addr = ('127.0.0.1', 9000)
    with ThreadingHTTPServer(addr, RequestHandler) as server:
        server.allow_reuse_address = True
        print(f'服务器启动: http://{addr[0]}:{addr[1]}')
        server.serve_forever()