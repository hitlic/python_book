class Test:
    def __init__(self):
        print(f'{id(self)} in __init__')

    def __new__(cls):
        o = object.__new__(cls)
        print(f'{id(o)} in __new__')
        return o


if __name__ == "__main__":
    obj = Test()
