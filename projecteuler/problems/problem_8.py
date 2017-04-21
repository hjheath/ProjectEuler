"""Problem eight of https://projecteuler.net"""

from pkg_resources import resource_string
from projecteuler.maths_functions import multiply


def problem_8():
    """Solution to problem eight."""
    file_contents = resource_string('projecteuler.data', 'problem_8.dat')
    file_as_string = file_contents.decode('utf-8')
    long_number = file_as_string.replace('\n', '')
    answer = 0

    for count in range(0, len(long_number) - 13):
        thirteen_digits = [int(digit) for digit in
                           long_number[count: count + 13]]

        # Any multiplication by zero will be zero.
        if 0 in thirteen_digits:
            continue

        product = multiply(thirteen_digits)
        if product > answer:
            answer = product

    return answer
