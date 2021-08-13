class TestIter:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5]

    def __getitem__(self, key):
        return self.values[key]


if __name__ == '__main__':
    ti = TestIter()
    for n in ti:
        print(n)
