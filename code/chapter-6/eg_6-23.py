from collections import abc


class TestSized:
    def __init__(self):
        self.num = 0

    def __len__(self):
        return self.num


if __name__ == '__main__':
    print(issubclass(TestSized, abc.Sized))
    ts = TestSized()
    print(isinstance(ts, abc.Sized))
