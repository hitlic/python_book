f = open('./file.txt')
while True:
    line = f.readline()
    if not line:
        break
    # 对文本行line进行处理
f.close()
