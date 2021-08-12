import pickle
import copyreg


class User:                                     # 旧版User类
    def __init__(self, name, age):
        self.name = name
        self.age = age


def unpickle_fun(obj_data):                     # 重建被序列化的对象
    print('reconstructing')
    return User(**obj_data)


def pickle_fun(obj):                            # 在序列化之前调用
    print('before pickling')
    return unpickle_fun, (obj.__dict__,)


copyreg.pickle(User, pickle_fun, unpickle_fun)  # 注册归约函数和重构函数

user = User('张三', 20)
user_pkl = pickle.dumps(user)                   # 序列化旧版User的对象

del User


class User:                                     # 新版User类
    def __init__(self, name, age, email='common@test.email'):
        self.name = name
        self.age = age
        self.email = email


user_recover = pickle.loads(user_pkl)           # 重构为新版User对象
print(user_recover.email)
