"""Problem 16 of https://projecteuler.net"""


def problem_16():
    """Solution to problem 16."""
    answer = sum([int(x) for x in str(2 ** 1000)])
    return answer


if __name__ == '__main__':
    print(problem_16())
