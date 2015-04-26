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
