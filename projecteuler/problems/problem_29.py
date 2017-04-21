"""Problem 29 of https://projecteuler.net"""


def problem_29():
    """Solution to problem 29."""
    powers = [a ** b for a in range(2, 101) for b in range(2, 101)]
    answer = len(set(powers))
    return answer
