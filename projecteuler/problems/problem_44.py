"""Problem 44 of https://projecteuler.net"""

from projecteuler.generators import pentagon_numbers
from projecteuler.inspectors import is_pentagonal


def problem_44():
    """Solution to problem 44."""
    pent_generator = pentagon_numbers()
    pents = {next(pent_generator)}
    while True:
        new_pent = next(pent_generator)
        for pent in pents:
            # It is faster to look up pentagonals we have already calculated
            if new_pent - pent not in pents:
                continue
            if not is_pentagonal(pent + new_pent):
                continue
            return new_pent - pent
        pents.add(new_pent)
