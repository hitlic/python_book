from functools import update_wrapper


class ClassDec():
    def __init__(self, fun):
        self.fun = fun
        update_wrapper(self, fun)

    def __call__(self):
        return self.fun()


@ClassDec
def test_fun():
    pass


if __name__ == '__main__':
    print(test_fun.__name__)
