"""Problem 30 of https://projecteuler.net"""


def problem_30():
    """Solution to problem 30."""
    count = 0
    # No solution can exist above 9^5 * 6.
    for number in range(2, (9 ** 5) * 6):
        digit_sum = sum([int(x) ** 5 for x in str(number)])
        if number == digit_sum:
            count += number

    answer = count
    return answer


if __name__ == '__main__':
    print(problem_30())
