"""Problem 26 of https://projecteuler.net"""


def problem_26():
    """Solution to problem 26."""
    longest = 0
    for number in range(2, 1000):
        divisor = 10
        pattern_dict = {}
        count = 0

        # Keep dividing by the number until we get a divisor we have seen
        # before. The number of iterations is the length of the pattern.
        while divisor not in pattern_dict:
            count += 1
            pattern_dict[divisor] = count
            remainder = divisor % number
            divisor = remainder * 10

        if count - pattern_dict[divisor] > longest:
            longest = count - pattern_dict[divisor]
            answer = number

    return answer


if __name__ == '__main__':
    print(problem_26())
