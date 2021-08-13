class LowerAttrs(type):
    def __new__(metacls, name, bases, attrs):
        new_attrs = {}
        for attr in attrs:
            if attr.startswith('__') and attr.endswith('__'):
                new_attrs[attr] = attrs[attr]
            else:
                new_attrs[attr.lower()] = attrs[attr]
        return super().__new__(metacls, name, bases, new_attrs)


class TestMetaclass(metaclass=LowerAttrs):
    def METHOD(self):
        print('METHOD')


if __name__ == '__main__':
    tm = TestMetaclass()
    tm.method()
    tm.METHOD()
