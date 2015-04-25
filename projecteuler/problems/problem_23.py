"""Problem 23 of https://projecteuler.net"""

import projecteuler.maths_functions as maths


def problem_23():
    """Solution to problem 23."""
    abundant_numbers = set()
    count = 0

    for number in range(1, 28124):
        if sum(maths.get_divisor_list(number)) > number:
            abundant_numbers.add(number)

        if not any((number - x in abundant_numbers) for x in abundant_numbers):
            count += number
    return count

if __name__ == '__main__':
    print(problem_23())
