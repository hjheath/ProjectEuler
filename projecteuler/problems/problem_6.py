"""Problem six of https://projecteuler.net"""


def problem_6():
    """Solution to problem six."""
    sum_of_squares = 0

    for x_value in range(1, 101):
        sum_of_squares += (x_value ** 2)

    square_of_sum = sum(range(1, 101)) ** 2
    answer = square_of_sum - sum_of_squares
    return answer


if __name__ == '__main__':
    print(problem_6())
