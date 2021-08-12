class TestSlot1:
    def __init__(self):
        self.x = 0
        self.y = 1


class TestSlot2:
    __slots__ = ['x', 'y']

    def __init__(self):
        self.x = 0
        self.y = 1


if __name__ == '__main__':
    ts1 = TestSlot1()
    ts2 = TestSlot2()
    print(ts1.__dict__)
    print(ts2.__dict__)
