"""Problem 36 of https://projecteuler.net"""

from projecteuler.inspectors import is_palindrome


def problem_36():
    """Solution to problem 36."""
    answers = [number for number in range(1000000) if db_palindrome(number)]
    return sum(answers)


def db_palindrome(number):
    """Check is a number is a double base palindrome"""
    if not is_palindrome(number):
        return False
    binary = bin(number)[2:]
    return binary == ''.join(reversed(binary))
