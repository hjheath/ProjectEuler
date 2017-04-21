"""Problem 25 of https://projecteuler.net"""

from projecteuler.generators import fibonaccis


def problem_25():
    """Solution to problem 25."""
    for count, number in enumerate(fibonaccis(), start=1):
        if len(str(number)) == 1000:
            answer = count
            break

    return answer
