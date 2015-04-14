"""Specialised mathematical functions e.g. multiply"""

from functools import reduce
import operator


def multiply(number_list):
    """
    Multiply together a list of numbers.

    :param number_list: The list of numbers to multiply together.

    :returns: An int or float containing the product of the number_list.
    """
    product = reduce(operator.mul, number_list)
    return product
