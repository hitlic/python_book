import shelve

class Test:
    pass

d1 = [1, 2.0, 3, 4+5j]
d2 = ("字符串数据", b"byte string")
d3 = {None, True, False}
d4 = Test()

# 序列化，以可写入方式打开文件
with shelve.open('shelve.data') as shelve_file:
    shelve_file['list'] = d1
    shelve_file['tuple'] = d2
    shelve_file['set'] = d3
    shelve_file['obj'] = d4

# 反序列化，以不可写入方式打开文件
with shelve.open('shelve.data', writeback=False) as shelve_file:
    for key, value in shelve_file.items():
        print(f'{key}：\t{value}')