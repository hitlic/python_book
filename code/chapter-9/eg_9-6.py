from numba import jit, int32


@jit(int32(int32, int32))
def f(x, y):
    return x + y


if __name__ == "__main__":
    print(f(2**31, 2**31 + 1))
