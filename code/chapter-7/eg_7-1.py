def fun(values, lst=[]):
    lst.extend(values)
    return lst


if __name__ == '__main__':
    print(fun([1, 2, 3]))
    print(fun([1, 2, 3]))
