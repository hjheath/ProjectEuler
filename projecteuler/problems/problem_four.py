"""Problem four of https://github.com/heathy/project_euler"""

from projecteuler.inspectors import is_palindrome


def problem_four():
    """Solution to problem four."""
    answer = 0

    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x * y
            if is_palindrome(product) and product > answer:
                answer = product
    return answer


if __name__ == '__main__':
    print(problem_four())
