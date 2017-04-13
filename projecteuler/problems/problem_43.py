"""Problem 43 of https://projecteuler.net"""

from math import ceil
from itertools import product
from itertools import permutations

from projecteuler.inspectors import is_pandigital


def problem_43():
    """Solution to problem 43."""
    # primes = [2, 3, 5, 7, 11, 13, 17]
    # triplets = [list(filter(repeats, multiples(prime, 100, 1000)))
    #             for prime in primes]
    # triplets
    # return triplets

    primes = [17, 13, 11, 7, 5, 3, 2]
    answers = []
    for perm in permutations('1234567890'):
        if perm[0] == '0':
            continue
        string = ''.join(perm)
        try:
            for index, prime in enumerate(primes):
                if not divisible_slice(string, prime, 7 - index):
                    raise RuntimeError
                print(string)
                answers.append(int(string))
        except RuntimeError:
            continue
    return sum(answers)


def multiples(number, minimum, maximum):
    """Return a list of multiples of a number between min and max"""
    x = number * ceil(minimum / number)
    multiples = []
    while x < maximum:
        multiples.append(x)
        x += number
    return multiples


def repeats(number):
    """Check if an integer has any repeated digits."""
    string = str(number)
    return len(string) == len(set(string))

def divisible_slice(string, divisor, start_index):
    """Check if a three digit slice of a string is divisible by divisor"""
    number = int(string[start_index:start_index + 3])
    return number % divisor == 0


if __name__ == '__main__':
    print(problem_43())

