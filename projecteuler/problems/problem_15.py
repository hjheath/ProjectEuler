"""Problem 15 of https://projecteuler.net"""


def problem_15():
    """Solution to problem 15."""
    combinations = 1
    grid_size = 20
    for i in range(1, grid_size + 1):
        # This is 2n choose n.
        combinations = combinations * (grid_size + i) // i
    return combinations


if __name__ == '__main__':
    print(problem_15())
