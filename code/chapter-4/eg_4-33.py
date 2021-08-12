from functools import lru_cache


@lru_cache
def fun(i):
    print(f'计算 {i} 的平方')
    return i**2


if __name__ == "__main__":
    for _ in range(3):
        print(fun(1))
