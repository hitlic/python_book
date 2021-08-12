import pickle

class TestClass:
    attr_cls = 1
    def __init__(self):
        self.attr_obj = 2

obj = TestClass()
obj.attr_obj = 3
obj_pkl = pickle.dumps(obj)     # 实例序列化

del obj
obj = pickle.loads(obj_pkl)     # 实例反序列化

print(obj.attr_cls)
print(obj.attr_obj)