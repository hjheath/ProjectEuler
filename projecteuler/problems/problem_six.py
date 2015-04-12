"""Problem six of https://projecteuler.net"""


def problem_six():
    """Solution to problem six."""
    sum_of_squares = 0

    for x in range(1, 101):
        sum_of_squares += (x ** 2)

    square_of_sum = sum(range(1, 101)) ** 2
    answer = square_of_sum - sum_of_squares
    return answer


if __name__ == '__main__':
    print(problem_six())
