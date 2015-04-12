"""Problem nine of https://projecteuler.net"""


def problem_nine():
    """Solution to problem nine."""
    # Use pen and paper to see a must be less than 500.
    triplet = [(a, b, 1000 - a - b) for a in range(1, 500) for b in range(1, a)
               if a ** 2 + b ** 2 == (1000 - a - b) ** 2]
    answer = triplet[0][0] * triplet[0][1] * triplet[0][2]
    return answer


if __name__ == '__main__':
    print(problem_nine())
