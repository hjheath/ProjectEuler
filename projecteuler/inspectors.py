"""Check for types of numbers."""

from itertools import takewhile
from math import sqrt
from projecteuler.generators import primes


def is_palindrome(number):
    """
    Check if a number is a palindrome.

    :param number: The int to check.

    :returns: True if the number is a palindrome, else False.
    """
    number_string = str(number)
    reversed_number = ''.join(reversed(number_string))
    return number_string == reversed_number


def is_prime(number):
    """
    Check if a number is prime.

    :param number: The int to check.

    :returns: True if the number is prime, else False.
    """
    if number < 2:
        return False
    for prime in takewhile(lambda x: x <= sqrt(number), primes()):
        if number % prime == 0:
            return False
    return True


def pandigital_product(multiplicand, multiplier):
    """
    Determine if two numbers form a pandigital product.

    :param multiplicand: The multiplicand in the product.

    :param multiplier: The multiplier in the product.

    :returns: The product if pandigital else False.
    """
    product = multiplicand * multiplier
    number_list = str(product) + str(multiplicand) + str(multiplier)
    number_set = set(number_list)
    if '0' in number_set:
        return False
    if len(number_set) == 9 and len(number_list) == 9:
        return product
    else:
        return False


def is_curious_fraction(numerator, denominator):
    """
    Determine if two numbers form a curious fraction.

    A curious fraction is where removing a number common to the numerator and
    denominator is equal to the original fraction.

    :param numerator: The numerator of the fraction as an int.

    :param denominator: The denominator of the fraction as an int.

    :returns: True if the fraction is curious else False.
    """
    fraction = numerator / denominator
    numerator = str(numerator)
    denominator = str(denominator)
    if len(numerator) == 1:
        return False
    if numerator.endswith('0') or denominator.endswith('0'):
        return False

    for number in numerator:
        new_numerator = numerator.replace(number, '', 1)
        new_denominator = denominator.replace(number, '', 1)
        new_fraction = int(new_numerator) / int(new_denominator)
        if new_fraction == fraction:
            return True

    return False
