import ctypes
lib = ctypes.cdll.LoadLibrary('./libaverage.so')
average = lib.average
average.argtypes = (ctypes.POINTER(ctypes.c_double),  # 指定参数为指针
                    ctypes.c_int)
average.restype = ctypes.c_double
lst = [1, 4, 2, 8, 5, 7]
param = (ctypes.c_double * len(lst))(*lst)  # 将列表转换为数组
print(average(param, len(lst)))
