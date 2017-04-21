"""Problem 24 of https://projecteuler.net"""

import itertools


def problem_24():
    """Solution to problem 24."""
    digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    permutation_list = list(itertools.permutations(digit_list))
    permutation_list.sort()
    answer = int(''.join(str(digit) for digit in permutation_list[999999]))
    return answer
