"""Problem 40 of https://projecteuler.net"""

from itertools import count

from projecteuler.maths_functions import multiply


def problem_40():
    """Solution to problem 40."""
    answers = []
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    length = 0
    counter = count(1)
    for index in indices:
        while length < index:
            value = str(next(counter))
            length += len(value)
        difference = length - index
        digit = value[-(difference + 1)]
        answers.append(int(digit))
    return multiply(answers)


if __name__ == '__main__':
    print(problem_40())
