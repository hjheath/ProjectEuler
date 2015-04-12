"""Problem three of https://projecteuler.net"""

from math import sqrt
from itertools import takewhile
from projecteuler.generators import primes

NUMBER = 600851475143


def problem_three():
    """Solution to problem three."""
    prime_factors = [x for x in takewhile(lambda x: x < sqrt(NUMBER), primes())
                     if NUMBER % x == 0]
    answer = prime_factors[-1]
    return answer


if __name__ == '__main__':
    print(problem_three())
