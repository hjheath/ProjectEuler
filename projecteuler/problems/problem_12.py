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
            half = number / 2
            number_plus = number + 1
            factor_number = factor_count(half) + factor_count(number_plus)
            if factor_number > 500:
                answer = int(half * number_plus)
                break
        else:
            half_plus = (number + 1) / 2
            factor_number = factor_count(half_plus) * factor_count(number)
            if factor_number > 500:
                answer = int(half_plus * number)
                break

    return answer
