from functools import wraps


def dec1(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print('dec1 before ...')
        result = fun(*args, **kwargs)
        print('dec1 after ...')
        return result
    return wrapper


def dec2(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print('dec2 before ...')
        result = fun(*args, **kwargs)
        print('dec2 after ...')
        return result
    return wrapper


@dec1
@dec2
def fun():
    print('完成fun的功能')


if __name__ == "__main__":
    fun()
