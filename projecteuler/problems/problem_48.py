"""Problem 44 of https://projecteuler.net"""


def problem_48():
    """Solution to problem 48."""
    return sum(x ** x for x in range(1, 1001)) % 10 ** 10

problem_48()
