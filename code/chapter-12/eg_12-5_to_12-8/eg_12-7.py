from wsgiref.simple_server import make_server
from wsgi_apps import first_wsgi_app

host = '127.0.0.1'
port = 9000
print(f"启动服务器，http://{host}:{port}\n")
server = make_server(host, port, first_wsgi_app)
server.serve_forever()
