"""Problem one of https://projecteuler.net"""


def problem_1():
    """Solution to problem one."""
    answer = sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])
    return answer


if __name__ == '__main__':
    print(problem_1())
