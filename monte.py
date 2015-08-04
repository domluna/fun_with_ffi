from __future__ import print_function
import argparse

import monte_py as mpy
import monte_go as go_lib
import monte_rs as rust_lib

parser = argparse.ArgumentParser(description="Run Monte Carlo Pi simulations in Python, Go or Rust.")
parser.add_argument('-l', '--lang', choices=['go', 'python', 'rust'],
                    default='python', help='language to run in, defaults to Python')
parser.add_argument('simulations', metavar='S', type=int,
                    help='Number of simulations')
parser.add_argument('needles', metavar='N', type=int,
                    help='Number of needles per simulation')

def run_python(sims, needles):
    return mpy.estimate_pi(sims, needles)

def run_go(sims, needles):
    return go_lib.estimate_pi(sims, needles)

def run_rust(sims, needles):
    return rust_lib.estimate_pi(sims, needles)

if __name__ == '__main__':
    args = parser.parse_args()

    sims = args.simulations
    needles = args.needles
    lang = args.lang
    print("Running {} simulations with {} needles in \"{}\".".format(sims, needles, lang))

    est = 0.0
    if lang == 'go':
        est = run_go(sims, needles)
    elif lang == 'rust':
        est = run_rust(sims, needles)
    else:
        est = run_python(sims, needles)
    print("Estimate Pi = {}".format(est))
