# 文件asgi_framework.py
from urllib.parse import parse_qs
from http.cookies import SimpleCookie
from framwork_utils import *

class ASGIFramework:
    def __init__(self, static='.'):
        self.handlers = {'GET': dict(), 'POST': dict()}
        self.statics = load_static(static)

    def route(self, path, method):                      # URL路由装饰器
        assert method in ['GET', 'POST'], '方法必须是GET或POST'
        return router(path, method, self.handlers)

    async def __call__(self, scope, receive, send):     # ASGI应用
        method = scope['method']                        # 请求方法
        path = scope['raw_path'].decode('utf-8')        # 请求路径
        cookie_str = dict(scope["headers"]).get(b'cookie', '') # Cookies
        req_obj = None
        if method == 'POST':
            event = await receive()                     # 接收请求事件
            query = event['body'].decode('utf-8')
            req_obj = parse_qs(query)                   # 处理请求参数
            sc = SimpleCookie()
            sc.load(cookie_str.decode('utf-8'))         # 处理Cookie
            req_obj['cookies'] = {k: m.value for k, m in sc.items()}
        handler = self.handlers[method].get(path, False)# 获取handler
        ck_dict = None
        if not handler:
            status = 404
            content = page404.encode('utf-8')
        else:
            status = 200
            content = await handler(req_obj)            # 执行handler
            if isinstance(content, tuple):
                content, ck_dict = content
            content = content.encode('utf-8')
        headers = [
            (b"Content-Length", b"%d" % len(content)),
            (b"Content-Type", b"text/html"),
        ]
        if ck_dict:
            set_ck = ';'.join([f'{k}={v}' for k, v in ck_dict.items()])
            headers.append((b'Set-Cookie', set_ck.encode('utf-8')))
        await send({                                    # 发送响应开始事件
            "type": "http.response.start",
            "status": status,
            "headers": headers
        })
        await send({                                    # 发送响应正文事件
            "type": "http.response.body",
            "body": content,
        })