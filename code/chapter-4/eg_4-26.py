import time
from functools import wraps


def run_time(fun):
    @wraps(fun)           # 使用wraps装饰器
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'函数{fun.__name__}的动行时间为{(end-start):.4}秒')
        return result
    return wrapper


@run_time
def fun():
    for _ in range(10):
        time.sleep(0.1)
    print('fun')


if __name__ == "__main__":
    print(fun.__name__)
