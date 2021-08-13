import time


def run_time(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'函数{fun.__name__}的动行时间为{(end-start):.4}秒')
        return result
    return wrapper


@run_time
def fun1():
    for _ in range(10):
        time.sleep(0.1)


@run_time
def fun2(t):
    for _ in range(t):
        time.sleep(0.1)


if __name__ == "__main__":
    fun1()
    fun2(10)
