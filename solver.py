import ctypes
import os

lib_path = os.path.join(os.getcwd(), 'librungekutta.dll')
lib = ctypes.cdll.LoadLibrary(lib_path)

solve = lib.solve
solve.argtypes = [ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_longdouble,
                  ctypes.c_int]
solve.restype = ctypes.c_longdouble