# 文件 rectangle.py
import ctypes

lib = ctypes.cdll.LoadLibrary('./librectangle.so')

class Rectangle:
    def __init__(self, width, height):
        self._methods = dict()
        self._methods['area'] = lib.area
        self._methods['perimeter'] = lib.perimeter
        lib.create.argtypes = (ctypes.c_double, ctypes.c_double)
        lib.create.restype = ctypes.c_void_p
        lib.area.argtypes = (ctypes.c_void_p,)
        lib.area.restype = ctypes.c_double
        lib.perimeter.argtypes = (ctypes.c_void_p,)
        lib.perimeter.restype = ctypes.c_double
        self.obj = lib.create(width, height)
        self._m_name = None

    def __getattr__(self, attr):
        self._m_name = attr
        return self.__call_method

    def __call_method(self, *args):
        return self._methods[self._m_name](self.obj, *args)