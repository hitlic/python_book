# 文件 pypy_test.py
import timeit


def bubble_sort(lst):
    """冒泡排序"""
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


setup_code = """
from __main__ import bubble_sort
import random
lst = list(range(1000))
random.shuffle(lst)
"""
t = timeit.timeit('bubble_sort(lst)', setup=setup_code, number=10)
print(t)
