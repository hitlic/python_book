import ctypes
lib = ctypes.cdll.LoadLibrary('./libadd.so')
add = lib.add
add.argtypes = (ctypes.c_double, ctypes.c_double)  # 参数的数据类型
add.restype = ctypes.c_double                      # 返回值的数据类型
print(add(1.0, 2))
