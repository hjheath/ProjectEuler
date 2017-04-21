"""Problem 35 of https://projecteuler.net"""

from itertools import takewhile
from projecteuler.generators import primes
from projecteuler.maths_functions import rotations


def problem_35():
    """Solution to problem 35."""
    potential_primes = (x for x in primes() if potential_prime(x))
    prime_set = {x for x in takewhile(lambda x: x < 1000000, potential_primes)}
    circular_primes = set()
    while prime_set:
        prime = prime_set.pop()
        prime_set.add(prime)
        rotation_set = rotations(prime)
        if rotation_set.issubset(prime_set):
            circular_primes.update(rotation_set)
        prime_set -= rotation_set
    return len(circular_primes)


def potential_prime(prime):
    """Return True if a prime could be circular."""
    if prime < 10:
        return True
    # If a prime contains any of the following it cannot be circular
    disallowed_digits = ['0', '2', '4', '6', '8', '5']
    if any(digit in str(prime) for digit in disallowed_digits):
        return False
    return True
