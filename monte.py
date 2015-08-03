from __future__ import print_function
import random

def estimate_pi(sims, needles):
    print("Running {} simulations with {} needles being dropped ...".format(sims, needles))
    trials = []
    for _ in xrange(sims):
        trials.append(simulate_pi(needles))

    mean = sum(trials) / sims
    return mean

# use a unit square
def simulate_pi(needles):
    hits = 0 # how many hits we hit the circle
    for _ in xrange(needles):
        x = random.uniform(-1., 1.)
        y = random.uniform(-1, 1.)
        if x*x + y*y <= 1.0:
            hits += 1
    return 4. * (hits / float(needles))


if __name__ == '__main__':
    mean = estimate_pi(1000, 10000)
    print(mean)
