import ctypes
lib = ctypes.cdll.LoadLibrary('./libdistance.so')

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]

distance = lib.distance
distance.argtypes = (ctypes.POINTER(Point),ctypes.POINTER(Point))
distance.restype = ctypes.c_double

p1 = Point(0, 0)
p2 = Point(3, 4)

print(distance(p1, p2))