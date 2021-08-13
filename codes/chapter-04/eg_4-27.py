import time
from functools import update_wrapper

def run_time(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'函数{fun.__name__}的动行时间为{(end-start):.4}秒')
        return result
    return update_wrapper(wrapper, fun)  # 使用update_wrapper函数
