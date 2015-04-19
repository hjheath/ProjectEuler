"""Specialised mathematical functions e.g. multiply"""

from functools import reduce
import operator
import math


def multiply(number_list):
    """
    Multiply together a list of numbers.

    :param number_list: The list of numbers to multiply together.

    :returns: An int or float containing the product of the number_list.
    """
    product = reduce(operator.mul, number_list)
    return product


def factor_count(number):
    """
    Calculate the number of factors of a number.

    :param number: The number to get the factors of (int).

    :returns: An int of the number of factors including the number itself.
    """
    count = 0
    root = math.sqrt(number)

    # Each factor below the sqrt has a corresponding factor above it.
    for integer in range(1, math.ceil(root)):
        if number % integer == 0:
            count += 2

    # Add to the count if the number is square.
    if root % 1 == 0:
        count += 1

    return count
