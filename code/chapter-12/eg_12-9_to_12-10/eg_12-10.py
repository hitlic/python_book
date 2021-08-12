from urllib.parse import parse_qs
from http import cookies


async def asgi_app(scope, receive, send):
    method = scope['method']                        # 请求方法
    code = ''
    info = ''
    if method == 'POST':
        event = await receive()                     # 接收请求事件
        # 处理请求参数
        query = event['body'].decode('utf-8')
        params = parse_qs(query)
        username = params.get('usertag')
        code = params.get('code', '')
        if username:
            username = username[0]
        if code:
            code = code[0]
        # 从cookie中读取上次提交的code，并将本次提交的code写入cookie
        cookie_str = dict(scope["headers"]).get('cookie', '')
        sc = cookies.SimpleCookie()
        sc.load(cookie_str)
        old_code = sc['code'].value if sc.get('code') else ''
        info = f'{username}提交成功!<br>{code}'
        if old_code:
            info = info+f'<br>上次提交的代码为:<br>{old_code}'

    with open('./index.html') as f:
        body = f.read()
    body = body.replace('<span id="info"/>', info).encode('utf-8')
    await send({                                    # 发送响应开始事件
        "type": "http.response.start",
        "status": 200,
        "headers": [
            (b"Content-Length", b"%d" % len(body)),
            (b"Content-Type", b"text/html"),
            (b"Set-Cookie", f'code={code}'.encode('utf-8')),
        ],
    })
    await send({                                    # 发送响应正文事件
        "type": "http.response.body",
        "body": body,
    })

if __name__ == "__main__":
    # 1. -- ASGIServer
    from asgi_server import ASGIServer
    server = ASGIServer(asgi_app)
    server.start()

    # # 2. -- Uvicorn
    # import uvicorn
    # uvicorn.run(asgi_app, host="127.0.0.1", port=9000)