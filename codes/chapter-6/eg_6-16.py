def class_dec1(class_deced):
    def new_method(self):
        print("执行装饰器添加的方法")
    class_deced.method = new_method
    return class_deced


@class_dec1
class TestClassDec:
    def method(self):
        print("执行被修饰类的方法")


if __name__ == '__main__':
    tc = TestClassDec()
    tc.method()
