"""Problem 28 of https://projecteuler.net"""


def problem_28():
    """Solution to problem 28."""
    count = 1
    for layer in range(3, 1002, 2):
        square = layer ** 2
        for number in range(4):
            corner = square - (number * (layer - 1))
            count += corner

    return count


if __name__ == '__main__':
    print(problem_28())
