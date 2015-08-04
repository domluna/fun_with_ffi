from ctypes import cdll, c_double, c_int32

lib = cdll.LoadLibrary("src/libgomonte.so")
estimate_pi = lib.EstimatePi
# need to change restype as it defaults to an int
estimate_pi.restype = c_double
estimate_pi.argtypes = [c_int32, c_int32]

# use lib
if __name__ == '__main__':
    res = estimate_pi(1000, 10000)
    print(res)
