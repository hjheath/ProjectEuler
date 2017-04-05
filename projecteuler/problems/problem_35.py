"""Problem 35 of https://projecteuler.net"""

from itertools import takewhile
from projecteuler.generators import primes


def problem_35():
    """Solution to problem 35."""
    potential_primes = (x for x in primes() if potential_prime(x))
    prime_list = [x for x in takewhile(lambda x: x < 100, potential_primes)]
    return prime_list



def potential_prime(prime):
    """Return True if a prime could be circular."""
    if prime < 10: return True
    # If a prime contains any of the following it cannot be circular
    disallowed_digits = ['0', '2', '4', '6', '8', '5']
    if any(digit in str(prime) for digit in disallowed_digits): return False
    return True


def rotations(number):
    number = str(number)
    result = set()
    for x, character in enumerate(number):
        result.add(number[x:] + number[:x])
    return result

if __name__ == '__main__':
    print(problem_35())
