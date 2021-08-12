class TestClass:
    pass


def get_class():
    class TestClass:
        pass
    return TestClass


if __name__ == '__main__':
    Test = TestClass       # 赋值给变量
    t = Test()
    print(t)
    lst = []
    lst.append(TestClass)  # 放入容器之中
    print(lst[0]())
    print(get_class()())          # 在函数中动态创建类，并返回
