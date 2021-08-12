# 文件wsgi_framework.py
from urllib.parse import parse_qs
from http.cookies import SimpleCookie
from framwork_utils import *

class WSGIFramework:
    def __init__(self, static='.'):
        self.handlers = {'GET': dict(), 'POST': dict()}
        self.statics = load_static(static)

    def route(self, path, method):                      # URL路由装饰器
        assert method in ['GET', 'POST'], '方法必须是GET或POST'
        return router(path, method, self.handlers)

    def __call__(self, env, start_response):            # WSGI应用
        method = env['REQUEST_METHOD']                  # 请求方法
        path = env['PATH_INFO']                         # 请求路径
        cookie_str = env['HTTP_COOKIE']                 # Cookies
        query = env['QUERY_STRING']
        req_obj = None
        if method == 'POST':
            size = int(env.get('CONTENT_LENGTH', 0))
            query = env['wsgi.input'].read(size).decode('utf-8')
            req_obj = parse_qs(query)                   # 处理请求参数
            sc = SimpleCookie()
            sc.load(cookie_str)                         # 处理Cookie
            req_obj['cookies'] = {k:m.value for k, m in sc.items()}
        handler = self.handlers[method].get(path, False)# 获取handler
        ck_dict = None
        if not handler:
            status = '404 Not Found'
            content = page404.encode('utf-8')
        else:
            status = '200 OK'
            content = handler(req_obj)                  # 执行handler
            if isinstance(content, tuple):
                content, ck_dict = content
            content = content.encode('utf-8')
        headers = [('Content-Type', 'text/html'),
                   ('Content-Length', str(len(content)))]
        if ck_dict:
            set_ck = ';'.join([f'{k}={v}' for k, v in ck_dict.items()])
            headers.append(('Set-Cookie', set_ck))
        start_response(status, headers)
        return [content]