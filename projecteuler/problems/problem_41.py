"""Problem 41 of https://projecteuler.net"""

from itertools import permutations

from projecteuler.inspectors import is_prime


def problem_41():
    """Solution to problem 41."""
    # All 8 and 9 digit pandigitals are divisible by 3.
    perms = [int(''.join(x)) for x in permutations('1234567')]
    return max(x for x in perms if is_prime(x))
