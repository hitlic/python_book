from functools import singledispatch


@singledispatch
def average(data):
    n = len(data)
    return sum(data)/n


@average.register(dict)   # 参数为字典时
def _(data):
    data = data.values()
    n = len(data)
    return sum(data)/n


@average.register(str)    # 参数为字符串时
def _(data):
    data = [float(i) for i in data.split(',')]
    n = len(data)
    return sum(data)/n


if __name__ == "__main__":
    print(average([1, 2, 3]))
    print(average({'a': 1, 'b': 2, 'c': 3}))
    print(average('1, 2, 3'))
