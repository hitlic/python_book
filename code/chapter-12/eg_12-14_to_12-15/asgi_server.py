# 文件asgi_server.py
import asyncio
from httplib import Parser

class ASGIServer:
    def __init__(self, app, host='127.0.0.1', port=9000):
        self.app = app
        self.host = host
        self.port = port

    async def __asgi_server(self, reader, writer):
        print(writer.get_extra_info('peername'))
        parser = Parser()
        msgs_receive = asyncio.Queue()           # HTTP请求事件消息队列
        while True:                              # 接收客户端HTTP请求
            data_recv = await reader.read(1024)
            parser.append(data_recv)
            if parser.is_ok(): break
        msg = self.make_msg(parser)              # 构造请求事件消息
        await msgs_receive.put(msg)
        scope = self.make_scope(parser)
        msgs_send = asyncio.Queue()              # HTTP响应事件消息队列
        await self.app(scope, msgs_receive.get,  # 异步调用ASGI应用
                       msgs_send.put)
        while True:                              # 处理HTTP响应事件
            msg = await msgs_send.get()
            if not self.send_msg(msg, writer): break
        await writer.drain()
        writer.close()

    def make_msg(self, parser):                   # 构造请求事件字典
        return { "type": "http.request",
                 "body": parser.body,
                 "more_body": False}

    def make_scope(self, parser):                 # 构造scope字典
        headers = [[name.encode('utf-8'), value.encode('utf-8')]
                   for name, value in parser.head_dict.items()]
        return { "type": "http",
                 "method": parser.req_method,
                 "scheme": "http",
                 "raw_path": parser.req_url.encode(),
                 "query_string": parser.query_string,
                 "path": parser.path,
                 "headers": headers}

    def send_msg(self, msg, writer):
        if msg["type"] == "http.response.start":  # 处理响应开始事件
            writer.write(b"HTTP/1.1 %d\r\n" % msg["status"])
            for header in msg["headers"]:
                writer.write(b"%s: %s\r\n" % (header))
            writer.write(b"\r\n")
        if msg["type"] == "http.response.body":  # 处理响应正文事件
            writer.write(msg["body"])
            return msg.get("more_body", False)
        return True

    def start(self):
        print(f"启动服务器，http://{self.host}:{self.port}")
        async def main():
            server = await asyncio.start_server(self.__asgi_server,
                                                self.host, self.port)
            await server.serve_forever()
        asyncio.run(main())


if __name__ == "__main__":
    from asgi_apps import first_asgi_app
    host, port = '127.0.0.1', 9000
    print(f'http://{host}:{port}')
    server = ASGIServer(first_asgi_app)
    server.start()
