class TestAttrAccess:
    def __getattr__(self, name):
        print(f"属性 {name} 不存在！")
        return None

    def __setattr__(self, name, value):
        print(f"为对象绑定属性{name}，值为{value}")
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f"销毁对象成员{name}")
        del self.__dict__[name]


if __name__ == '__main__':
    taa = TestAttrAccess()
    taa.x
    taa.x = 1
    del taa.x
