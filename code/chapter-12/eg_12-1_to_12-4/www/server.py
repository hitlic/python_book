from http.server import HTTPServer, CGIHTTPRequestHandler

addr = ('127.0.0.1', 9000)
server = HTTPServer(addr, CGIHTTPRequestHandler)
print(f'服务器启动 http://{addr[0]}:{addr[1]}')
server.serve_forever()
