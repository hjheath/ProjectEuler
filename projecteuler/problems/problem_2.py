"""Problem two of https://projecteuler.net"""

from itertools import takewhile
from projecteuler.generators import fibonaccis


def problem_2():
    """Solution to problem two."""
    fibonacci_numbers = [x for x in
                         takewhile(lambda x: x < 4000000, fibonaccis())]
    answer = sum(y for y in fibonacci_numbers if y % 2 == 0)
    return answer

if __name__ == '__main__':
    print(problem_2())
