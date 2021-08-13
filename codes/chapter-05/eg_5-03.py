class Test:
    def __init__(self, *args, **kwargs):
        print(f'{args} in __init__')
        print(f'{kwargs} in __init__')

    def __new__(cls, *args, **kwargs):
        o = object.__new__(cls)
        print(f'{args} in __new__')
        print(f'{kwargs} in __new__')
        return o


if __name__ == "__main__":
    obj = Test(1, x=2)
