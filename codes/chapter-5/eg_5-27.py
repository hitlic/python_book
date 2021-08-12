from collections import defaultdict

class ReadOnlyDictMixin:
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            old_value = super().__getitem__(key)
            print(f'字典中已存在{key}值，不能修改！')
            value = old_value
        return super().__setitem__(key, value)

class ReadOnlyDict(ReadOnlyDictMixin, defaultdict):
    pass


if __name__ == "__main__":
    d = ReadOnlyDict()
    d['x'] = 1
    d['x'] = 2
    print(d.items())
