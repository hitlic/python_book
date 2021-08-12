import ctypes
lib = ctypes.cdll.LoadLibrary('./libswap.so')
swap = lib.swap
swap.argtypes = (ctypes.POINTER(ctypes.c_double),  # 参数的数据类型
                 ctypes.POINTER(ctypes.c_double))
swap.restype = None                                # 返回值的数据类型
x = ctypes.c_double(1.0)
y = ctypes.c_double(2.0)
swap(x, y)                                         # 调用函数
print(x, y)
