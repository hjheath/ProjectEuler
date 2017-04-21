"""Problem 33 of https://projecteuler.net"""

from fractions import Fraction

from projecteuler.inspectors import is_curious_fraction
from projecteuler.maths_functions import multiply


def problem_33():
    """Solution to problem 33."""
    curious_fractions = []
    for denominator in range(1, 100):
        # Only try fractions less than one.
        for numerator in range(1, denominator):
            if is_curious_fraction(numerator, denominator):
                curious_fractions.append(Fraction(numerator, denominator))

    product = multiply(curious_fractions)
    answer = product.denominator
    return answer
