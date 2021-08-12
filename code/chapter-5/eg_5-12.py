class TestClassMethod:
    class_value = 0

    @classmethod
    def class_method(cls):
        print(cls.class_value)


if __name__ == "__main__":
    TestClassMethod.class_method()
    tcm = TestClassMethod()
    tcm.class_method()
