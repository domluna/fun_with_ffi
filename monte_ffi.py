from ctypes import cdll, c_double, c_uint32

lib = cdll.LoadLibrary("monte-rs/target/release/libmonte.dylib")
estimate_pi = lib.estimate_pi
# need to change restype as it defaults to an int
estimate_pi.restype = c_double
estimate_pi.argtypes = [c_uint32, c_uint32]

# use lib
if __name__ == '__main__':
    res = estimate_pi(100, 1000)
    print(res)
