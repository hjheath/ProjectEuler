"""Problem ten of https://projecteuler.net"""

from itertools import takewhile
from projecteuler.generators import primes


def problem_10():
    """Solution to problem ten."""
    prime_list = [x for x in takewhile(lambda x: x < 2000000, primes())]
    answer = sum(prime_list)
    return answer

if __name__ == '__main__':
    print(problem_10())
