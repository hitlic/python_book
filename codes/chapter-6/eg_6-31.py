import pickle

# 待序列化数据
data = {
    'list': [1, 2.0, 3, 4+5j],
    'tuple': ("字符串数据", b"byte string"),
    'set': {None, True, False}
}

# 序列化
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# 反序列化
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
