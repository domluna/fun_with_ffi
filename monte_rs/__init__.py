from ctypes import cdll, c_double, c_int32
import os

lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "target/release/libmonte.dylib"))
# need to change restype as it defaults to an int
lib.estimate_pi.restype = c_double
lib.estimate_pi.argtypes = [c_int32, c_int32]

def estimate_pi(sims, needles):
    return lib.estimate_pi(sims, needles)
