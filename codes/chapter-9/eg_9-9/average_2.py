import ctypes
lib = ctypes.cdll.LoadLibrary('./libaverage.so')

average_ = lib.average
average_.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_int)
average_.restype = ctypes.c_double


def average(lst):
    param = (ctypes.c_double * len(lst))(*lst)
    return average_(param, len(lst))


lst = [1, 4, 2, 8, 5, 7]
print(average(lst))
