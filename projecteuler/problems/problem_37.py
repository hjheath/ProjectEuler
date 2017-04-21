"""Problem 37 of https://projecteuler.net"""

from projecteuler.generators import primes


def problem_37():
    """Solution to problem 37."""
    answers = []
    prime_set = set()
    prime_generator = primes()
    while len(answers) < 11:
        prime = next(prime_generator)
        prime_set.add(prime)
        if prime < 10:
            continue
        try:
            check_truncated(prime, prime_set, truncate_right)
            check_truncated(prime, prime_set, truncate_left)
        except RuntimeError:
            continue
        answers.append(prime)
    return sum(answers)


def truncate_right(number):
    """Truncate a number to the right"""
    truncated = str(number)[:-1]
    if truncated:
        return int(truncated)


def truncate_left(number):
    """Truncate a number to the left"""
    truncated = str(number)[1:]
    if truncated:
        return int(truncated)


def check_truncated(number, prime_set, truncate_function):
    """Check all truncated numbers are prime."""
    while number >= 10:
        number = truncate_function(number)
        if number not in prime_set:
            raise RuntimeError
