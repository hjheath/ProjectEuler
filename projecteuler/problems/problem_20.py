"""Problem 20 of https://projecteuler.net"""

from math import factorial


def problem_20():
    """Solution to problem 20."""
    big_number = factorial(100)
    answer = sum(int(x) for x in str(big_number))
    return answer


if __name__ == '__main__':
    print(problem_20())
