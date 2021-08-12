def add_property(prop_name, value):
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            print(f"添加属性{prop_name}")
            self.__dict__[prop_name] = value
            result = method(self, *args, **kwargs)
            del self.__dict__[prop_name]
            print(f"删除属性{prop_name}")
            return result
        return wrapper
    return decorator


class TestMethodDec:
    @add_property('new_property', 100)
    def method(self):
        print(self.new_property)


if __name__ == '__main__':
    tm = TestMethodDec()
    tm.method()
