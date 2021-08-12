class Left:
    def __init__(self, v):
        self.v = v


class Right:
    def __init__(self, v):
        self.v = v

    def __radd__(self, o):
        return self.v + o.v

    def __rsub__(self, o):
        return o.v - self.v


if __name__ == '__main__':
    l = Left(2)
    r = Right(1)
    print(l + r)
    print(l - r)
    print(r + l)
