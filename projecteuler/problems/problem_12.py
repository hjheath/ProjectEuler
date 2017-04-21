"""Problem 12 of https://projecteuler.net"""

from projecteuler.maths_functions import factor_count
from itertools import count


def problem_12():
    """Solution to problem 12."""
    # Triangle number can be defined as n(n+1)/2.
    # n and n+1 share only the factor 1.
    # Therefore the total number of factors of a triangle number is the product
    # of the factors of n/2 and n+1 or (n+1)/2 and n depending on if n is
    # even or odd.
    for number in count():
        if number % 2 == 0:
            factor_one = number / 2
            factor_two = number + 1
        else:
            factor_one = (number + 1) / 2
            factor_two = number
        total_factors = factor_count(factor_one) * factor_count(factor_two)
        if total_factors > 500:
            return int(factor_one * factor_two)
