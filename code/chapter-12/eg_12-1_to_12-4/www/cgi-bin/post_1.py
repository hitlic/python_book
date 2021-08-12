#!/path/to/envs/env_name/bin/python
# 该路径需根据Python环境进行设置

import cgi
import os
import http.cookies

form = cgi.FieldStorage()
username = form.getvalue('usertag')
code = form.getvalue('code')

print("Content-type: text/html")
print(f"Set-Cookie: code={code}")                     # 设置Cookie项
print('\r\n')

old_code = None
sc = http.cookies.SimpleCookie()
sc.load(os.environ.get('HTTP_COOKIE'))
old_code = sc.get('code', None)
if old_code:
    old_code = old_code.value

if username is None or code is None:
    print("<center><h1>请求失败，参数错误！</h1></center>")
else:
    with open('./index.html') as f:
        html = f.read()
        info = f'{username} 提交成功! <br>{code}'
        if old_code:
            info = info + f'<br>上次提交的代码为:<br>{old_code}'
        html = html.replace('<span id="info"/>', info)
        print(html)
