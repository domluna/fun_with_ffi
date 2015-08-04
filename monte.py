from __future__ import print_function
import argparse

import monte_py as mpy
import monte_go as go_lib
import monte_rs as rust_lib

def run_python(sims, needles):
    print("Running Python")
    return mpy.estimate_pi(sims, needles)

def run_go(sims, needles):
    print("Running Go")
    return go_lib.estimate_pi(sims, needles)

def run_rust(sims, needles):
    print("Running Rust")
    return rust_lib.estimate_pi(sims, needles)

if __name__ == '__main__':
    sims = 100
    needles = 100

    # print("Running {} simulations with {} needles being dropped ...".format(sims, needles))
    print(run_python(sims, needles))
    print(run_go(sims, needles))
    print(run_rust(sims, needles))
