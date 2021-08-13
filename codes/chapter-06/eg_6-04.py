class PointwiseVector:
    def __init__(self, value):
        self.v = value

    def check_len(self, o):
        if len(o.v) != len(self.v):
            return False
        return True

    def __add__(self, o):
        if not self.check_len(o):
            return None
        return self.__class__([v1 + v2 for v1, v2 in zip(self.v, o.v)])

    def __sub__(self, o):
        if not self.check_len(o):
            return None
        return self.__class__([v1 - v2 for v1, v2 in zip(self.v, o.v)])

    def __mul__(self, o):
        if not self.check_len(o):
            return None
        return self.__class__([v1 * v2 for v1, v2 in zip(self.v, o.v)])

    def __truediv__(self, o):
        if not self.check_len(o):
            return None
        return self.__class__([v1 / v2 for v1, v2 in zip(self.v, o.v)])


if __name__ == '__main__':
    o1 = PointwiseVector([1, 2, 3])
    o2 = PointwiseVector([1, 2, 3])
    print((o1 + o2).v)
    print((o1 - o2).v)
    print((o1 * o2).v)
    print((o1 / o2).v)
