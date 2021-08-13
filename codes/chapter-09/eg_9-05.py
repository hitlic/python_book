# 本例需在命令行中运行

import timeit
from numba import jit


def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac


@jit
def factorial_jit(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac
