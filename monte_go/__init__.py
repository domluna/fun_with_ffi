from ctypes import cdll, c_double, c_int32
import os

lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "src/libgomonte.so"))
estimate_pi = lib.EstimatePi
lib.EstimatePi.restype = c_double
lib.EstimatePi.argtypes = [c_int32, c_int32]

def estimate_pi(sims, needles):
    return lib.EstimatePi(sims, needles)
