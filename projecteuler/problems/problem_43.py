"""Problem 43 of https://projecteuler.net"""

from itertools import permutations


def problem_43():
    """Solution to problem 43."""
    # Slight cop out because the brute force was too slow:
    # d6 must be 0 or 5 (divisible by 5)
    # d6d7d8 is divisible by 11. This implies d6 is 5 (011 is not pandigital)

    primes = [17, 13, 11, 7, 5, 3, 2]
    answers = []
    for perm in permutations('1234567890'):
        if perm[0] == '0' or perm[5] != '5':
            continue
        try:
            for index, prime in enumerate(primes):
                if not _divisible_slice(perm, prime, 7 - index):
                    raise RuntimeError
            answers.append(int(''.join(perm)))
        except RuntimeError:
            continue
    return sum(answers)


def _divisible_slice(perm, divisor, start_index):
    """Check if a three digit slice of a permutation is divisible by divisor"""
    perm_slice = perm[start_index:start_index + 3]
    number = int(''.join(perm_slice))
    return number % divisor == 0


if __name__ == '__main__':
    print(problem_43())
