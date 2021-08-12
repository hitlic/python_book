#!/path/to/envs/env_name/bin/python
# 该路径需根据Python环境进行设置

print("Content-type: text/html")
print("\r\n")

head = '<head>' \
    '<title>第一个CGI程序</title>' \
       '</head>'
body = '<body>' \
    '<center><h1>第一个CGI程序</h1></center>' \
       '</body>'
print('<html>')
print(head)
print(body)
print('</html>')
