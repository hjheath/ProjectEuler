"""Problem four of https://projecteuler.net"""

from projecteuler.inspectors import is_palindrome


def problem_4():
    """Solution to problem four."""
    answer = 0

    for x_value in range(100, 1000):
        for y_value in range(100, 1000):
            product = x_value * y_value
            if is_palindrome(product) and product > answer:
                answer = product
    return answer
