"""Problem seven of https://projecteuler.net"""

from projecteuler.generators import primes


def problem_7():
    """Solution to problem seven."""
    counter = 0

    for prime in primes():
        counter += 1
        if counter == 10001:
            answer = prime
            break
    return answer

if __name__ == '__main__':
    print(problem_7())
