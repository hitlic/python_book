class TestDict:
    x_class = 0

    def __init__(self):
        self.x_obj = 1


if __name__ == '__main__':
    print(TestDict.__dict__)
    td = TestDict()
    print(td.__dict__)
