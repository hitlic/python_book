# 文件 wsgi_apps.py
def first_wsgi_app(env, start_response):
    content = f'''
    <html>
    <head>
        <meta charset="UTF-8">
        <title>第一个WSGI应用</title>
    </head>
    <body>
        <center><h1>第一个WSGI应用</h1></center>
        请求路径：{env['PATH_INFO']} <br>
        请求参数：{env['QUERY_STRING']}
    </body>
    </html>'''.encode('utf-8')
    status = '200 OK'
    headers = [('Content-Type', 'text/html'), 
               ('Content-Length', str(len(content)))]
    start_response(status, headers)
    return [content]