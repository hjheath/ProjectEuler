"""Problem 45 of https://projecteuler.net"""

from projecteuler.generators import triangle_numbers
from projecteuler.inspectors import is_pentagonal, is_hexagonal


def problem_45():
    """Solution to problem 45."""
    count = 0
    triangle_generator = triangle_numbers()
    while True:
        number = next(triangle_generator)
        if not is_hexagonal(number):
            continue
        if not is_pentagonal(number):
            continue
        count += 1
        if count == 3:
            return number
