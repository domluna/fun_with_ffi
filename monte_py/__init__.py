import random

def estimate_pi(sims, needles):
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
