from wsgi_framework import WSGIFramework
app = WSGIFramework()


@app.route('/', 'GET')
def index_get(_):
    content = app.statics['index.html']
    return content


@app.route('/', 'POST')
def index_post(request):
    content = app.statics['index.html']
    username = request.get('usertag')
    code = request.get('code')
    old_code = request.get('cookies').get('code', '')
    if username:
        username = username[0]
    if code:
        code = code[0]
    info = f'{username}提交成功!<br>{code}'
    if old_code:
        info = info+f'<br>上次提交的代码为:<br>{old_code}'
    content = content.replace(r'<span id="info"/>', info)
    return content, {'code':code}


if __name__ == '__main__':
    # -- WSGIServer
    from wsgi_server import WSGIServer
    server = WSGIServer(app)
    server.start()

    # # -- simple_server
    # from wsgiref.simple_server import make_server
    # print("启动服务器，http://127.0.0.1:9000\n")
    # server = make_server('127.0.0.1', 9000, app)
    # server.serve_forever()

    # # waitress
    # import waitress
    # waitress.serve(app, listen='127.0.0.1:9000')
