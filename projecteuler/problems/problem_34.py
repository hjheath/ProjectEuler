"""Problem 34 of https://projecteuler.net"""


def problem_34():
    """Solution to problem 34."""
    answers = []
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    # The upper bound is 7 * 9! because it is impossible for an 8 digit number
    # to equal the sum of its factorials. Use 45000 for speed
    for number in range(10, 41000):
        digits = [int(digit) for digit in str(number)]
        factorial_sum = sum([factorials[digit] for digit in digits])
        if factorial_sum == number:
            answers.append(number)

    return sum(answers)
