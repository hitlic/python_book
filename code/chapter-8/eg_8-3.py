f = open('./binfile.bin', 'wb')  # 以二进制写入模式打开文件
f.write('二进制字节串'.encode('utf-8')) # 字符串编码为字节串，并写入文件
f.close()

f = open('./binfile.bin', 'rb')  # 以二进制读取模式打开文件
content = f.read()
f.close()
print("解码前：", content)
content = content.decode('utf-8')       # 对字节串进行解码
print("解码后：", content)