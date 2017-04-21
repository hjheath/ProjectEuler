"""Problem 27 of https://projecteuler.net"""

from itertools import takewhile, count
from projecteuler.generators import primes


def problem_27():
    """Solution to problem 27."""
    prime_list = [x for x in takewhile(lambda x: x < 1000, primes())]
    prime_list += [-x for x in prime_list]
    longest = 0

    # Notice the two formulae generate the same set of primes and expect the
    # answer to generate the same primes.
    possible_primes = set((x ** 2) + x + 41 for x in range(40))

    # a, b and n are used as names to correspond to the formula in the problem.
    for a in range(-999, 999, 2):
        for b in prime_list:
            for n in count(0):
                quadratic = (n ** 2) + (a * n) + b
                if quadratic not in possible_primes:
                    if n > longest:
                        longest = n
                        answer = a * b
                    break

    return answer
