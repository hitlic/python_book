class TestStaticMethod:
    @staticmethod
    def static_method():
        print('这里是静态方法！')

if __name__ == "__main__":
    TestStaticMethod.static_method()
    tsm = TestStaticMethod()
    tsm.static_method()