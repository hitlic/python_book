import pickle


def test_fun():
    return 'Hello Pickle'


class TestClass:
    pass


if __name__ == '__main__':
    fun_pkl = pickle.dumps(test_fun)      # 函数序列化
    class_pkl = pickle.dumps(TestClass)   # 类序列化
    fun = pickle.loads(fun_pkl)           # 函数反序列化
    print(fun())
    test_class = pickle.loads(class_pkl)  # 类反序列化
    obj = test_class()
    del test_fun                          # 删除函数定义
    del TestClass                         # 函数类定义
    fun = pickle.loads(fun_pkl)           # 再次反序列化函数
    test_class = pickle.loads(class_pkl)  # 再次反序列化类
