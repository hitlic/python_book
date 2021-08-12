from urllib.parse import parse_qs
import http.cookies

def wsgi_app(env, start_response):
    method = env['REQUEST_METHOD']                        # 请求方法
    query = env['QUERY_STRING']                           # 请求参数
    if not query and method == 'POST':
        content_len = int(env['CONTENT_LENGTH'])
        query = env['wsgi.input'].read(content_len).decode('utf-8')

    with open('index.html') as f:                         # 读取HTML文档
        content = f.read()

    headers = [('Content-Type', 'text/html')]             # 响应头
    info = ''
    if method == 'POST':                                  # 响应POST请求
        # 处理请求参数
        params = parse_qs(query)
        username = params.get('usertag')
        code = params.get('code', '')
        if username:
            username = username[0]
        if code:
            code = code[0]

        # 从cookie中读取上次提交的code，并将本次提交的code写入cookie
        cookie_str = env.get('HTTP_COOKIE', '')
        sc = http.cookies.SimpleCookie()
        sc.load(cookie_str)
        old_code = sc['code'].value if sc.get('code') else ''
        info = f'{username}提交成功!<br>{code}'
        if old_code:
            info = info+f'<br>上次提交的代码为:<br>{old_code}'
        headers.append(('Set-Cookie', f'code={code}'))    # 写入cookie

    content = content.replace('<span id="info"/>', info).encode('utf-8')
    headers.append(('Content-Length', str(len(content)))) # 请求正文长度
    start_response('200 OK', headers)
    return [content]

if __name__ == "__main__":
    # 1.-- WSGIServer
    from wsgi_server import WSGIServer
    server = WSGIServer(wsgi_app)
    server.start()

    # # 2.-- simple_server
    # from wsgiref.simple_server import make_server
    # print("启动服务器，http://127.0.0.1:9000")
    # server = make_server('127.0.0.1', 9000, wsgi_app)
    # server.serve_forever()

    # # 3.-- waitress
    # import waitress
    # waitress.serve(wsgi_app, listen='127.0.0.1:9000')