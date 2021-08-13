class PointwiseVector:
    def __init__(self, value):
        self.v = value

    # ...
    # 此处略去其他方法的定义
    # ...

    def __str__(self):
        print('__str__方法被调用')
        return str(self.v)

    def __repr__(self):
        print('__repr__方法被调用')
        return str(self.v)


if __name__ == '__main__':
    pv = PointwiseVector([1, 2, 3])
    print(pv)
    str(pv)
    pv
    repr(pv)
