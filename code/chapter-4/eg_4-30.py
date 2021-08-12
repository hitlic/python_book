def param_dec(arg1, arg2):
    def dec(fun):
        def wrapper(*args, **kw):
            print(f"before actions based on {arg1} and {arg2} ...")
            result = fun(*args, **kw)
            print(f"after actions based on {arg1} and {arg2} ...")
            return result
        return wrapper
    return dec


@param_dec('arg1', 'arg2')
def fun():
    print('完成fun的功能')


if __name__ == "__main__":
    fun()
