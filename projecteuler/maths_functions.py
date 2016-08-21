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


def get_divisor_list(number):
    """
    Calculate the divisors of a number.

    :param number: The number to get the divisors of (int).

    :returns: An list of divisors (ints) not including the number itself.
    """
    root = math.sqrt(number)
    factor_list = []

    # Each factor below the sqrt has a corresponding factor above it.
    for integer in range(1, math.ceil(root)):
        if number % integer == 0:
            factor_list.extend([integer, number // integer])

    # Add the square root if the number is square.
    if root % 1 == 0:
        factor_list.append(int(root))

    factor_list.remove(number)
    factor_list.sort()
    return factor_list


def factorial(number):
    """
    Recursively calculate the factorial of a number.

    :param number: A positive integer.

    :returns: The factorial (int).
    """
    factorial = 1
    for num in range(1, number + 1):
        factorial *= num
    return factorial
