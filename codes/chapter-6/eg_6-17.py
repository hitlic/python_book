def class_dec2(class_deced):
    class Inner:
        def __init__(self, *args, **kwargs):
            self.class_obj = class_deced(*args, **kwargs)  # 代理对象

        def method(self):
            print("执行装饰器中类的方法")
            return self.class_obj.method()
    return Inner


@class_dec2
class TestClassDec:
    def method(self):
        print("执行被修饰的方法")


if __name__ == '__main__':
    tm = TestClassDec()
    tm.method()
