from asgi_framework import ASGIFramework
app = ASGIFramework()


@app.route('/', 'GET')
async def index_get(_):
    content = app.statics['index.html']
    return content


@app.route('/', 'POST')
async def index_post(request):
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
    return content, {'code': code}


if __name__ == '__main__':
    # 1. -- ASGIServer
    from asgi_server import ASGIServer
    server = ASGIServer(app)
    server.start()

    # # 2. -- Uvicorn
    # import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=9000)
