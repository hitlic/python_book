import time
from datetime import datetime
from functools import wraps


def run_time(unit):
    def dec(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = fun(*args, **kwargs)
            end = datetime.now()
            if unit == 'ms':
                time_str = f'{(end-start).total_seconds()*1000:.0f}毫秒'
            elif unit == 'us':
                time_str = f'{(end-start).total_seconds()*10**6:.0f}微秒'
            else:
                time_str = f'{(end-start).total_seconds():.0f}秒'
            print(f'函数{fun.__name__}的动行时间为{time_str}')
            return result
        return wrapper
    return dec


@run_time('s')
def fun1():
    for _ in range(10):
        time.sleep(0.1)


@run_time('ms')
def fun2():
    for _ in range(10):
        time.sleep(0.1)


@run_time('us')
def fun3():
    for _ in range(10):
        time.sleep(0.1)


if __name__ == "__main__":
    fun1()
    fun2()
    fun3()
