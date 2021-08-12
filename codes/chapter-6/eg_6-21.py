import types


class ClassDec():
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print('执行__call__')
        return self.fun(*args, **kwargs)

    def __get__(self, obj, cls):
        print('执行__get__')
        print(obj)
        print(cls)
        return types.MethodType(self, obj)


@ClassDec
def fun():
    print('执行被修饰函数')


class TestDec:
    @ClassDec
    def method(self):
        print('执行被修饰方法')


if __name__ == '__main__':
    fun()
    td = TestDec()
    td.method()
