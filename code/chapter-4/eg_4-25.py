import time


def run_time(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'函数{fun.__name__}的动行时间为{(end-start):.4}秒')
        return result
    wrapper.__name__ = fun.__name__  # 保存被修饰函数的__name__属性
    wrapper.__doc__ = fun.__doc__    # 保存被修饰函数的__doc__属性
    return wrapper


@run_time
def fun():
    for _ in range(10):
        time.sleep(0.1)


if __name__ == "__main__":
    print(fun.__name__)
