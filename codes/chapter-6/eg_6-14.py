def add_property(method):
    def wrapper(self):         # 方法的特殊参数 self
        print("添加一个属性")
        self.new_property = 0  # 添加属性
        result = method(self)  # 调用被修饰方法，传入特殊参数
        del self.new_property  # 删除属性
        print("删除属性")
        return result
    return wrapper


class TestMethodDec:
    @add_property
    def method(self):
        print(self.new_property)


if __name__ == '__main__':
    tm = TestMethodDec()
    tm.method()
