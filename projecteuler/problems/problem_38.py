"""Problem 38 of https://projecteuler.net"""

from projecteuler.inspectors import is_pandigital


def problem_38():
    """Solution to problem 38."""
    # The answer must be greater or equal than 918273645.
    # Therefore only look at concatenated products of 9182-9999 and (1, 2)
    answers = []
    for number in range(9182, 9999):
        product = str(number) + str(number * 2)
        if is_pandigital(product):
            answers.append(int(product))
    return max(answers, default=918273645)

if __name__ == '__main__':
    print(problem_38())
