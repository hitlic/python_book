def dec1(fun):
    def wrapper(*args, **kwargs):
        print('dec1')
        return fun(*args, **kwargs)
    return wrapper


def dec2(fun):
    def wrapper(*args, **kwargs):
        print('dec2')
        return fun(*args, **kwargs)
    return wrapper


@dec1
@dec2
def fun():
    print('fun')


if __name__ == "__main__":
    fun()
