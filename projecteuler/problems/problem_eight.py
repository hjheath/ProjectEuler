"""Problem eight of https://github.com/heathy/project_euler"""

from pkg_resources import resource_string
from functools import reduce
import operator


def problem_eight():
    """Solution to problem eight."""
    file_conents = resource_string('projecteuler.data', 'problem_eight.dat')
    file_as_string = file_conents.decode('utf-8')
    long_number = file_as_string.replace('\n', '')
    answer = 0

    for count in range(0, len(long_number) - 13):
        thirteen_digits = [int(digit) for digit in
                           long_number[count: count + 13]]

        # Any multiplication by zero will be zero.
        if 0 in thirteen_digits:
            continue

        product = reduce(operator.mul, thirteen_digits)
        if product > answer:
            answer = product

    return answer


if __name__ == '__main__':
    print(problem_eight())
