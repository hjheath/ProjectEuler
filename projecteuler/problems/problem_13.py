"""Problem 13 of https://projecteuler.net"""

from pkg_resources import resource_string


def problem_13():
    """Solution to problem 13."""
    file_conents = resource_string('projecteuler.data', 'problem_13.dat')
    file_as_string = file_conents.decode('utf-8')
    numbers = file_as_string.split('\n')
    # Only the first 11 digits can affect the first 10 digits of the sum.
    significant_digits = [int(number[:11]) for number in numbers]
    start_of_sum = sum(significant_digits)
    # Use a string to perform a slice, but return the answer as an int.
    answer = int(str(start_of_sum)[:10])
    return answer


if __name__ == '__main__':
    print(problem_13())
