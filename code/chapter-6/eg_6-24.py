from collections import abc

@abc.MutableSequence.register                # 使用装饰器注册虚拟子类
class RegisterAbc:
    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        self._values[index] = value

    def __delitem__(self, index):
        del self._values[index]

    def insert(self, index, value):
        self._values.insert(index, value)

# abc.MutableSequence.register(RegisterAbc)  # 使用函数注册虚拟子类

if __name__ == '__main__':
    print(issubclass(RegisterAbc, abc.MutableSequence))
    ra = RegisterAbc([1, 2, 3])
    print(isinstance(ra, abc.MutableSequence))
