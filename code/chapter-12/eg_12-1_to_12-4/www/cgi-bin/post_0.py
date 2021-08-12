#!/path/to/envs/env_name/bin/python
# 该路径需根据Python环境进行设置

import cgi

print("Content-type: text/html")
print('\r\n')

fields = cgi.FieldStorage()
username = fields.getvalue('usertag')
code = fields.getvalue('code')

print('<html><head><title>作业提交</title></head>')
if username is None and code is None:
    print("<center><h1>请求失败，参数错误！</h1></center>")
else:
    with open('./index.html') as f:
        html = f.read()
        html = html.replace('<span id="info"/>',
                            f'{username} 提交成功! <br>{code}')
        print(html)
print('</html>')