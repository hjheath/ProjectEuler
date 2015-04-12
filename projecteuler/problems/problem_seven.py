"""Problem seven of https://github.com/heathy/project_euler"""

from projecteuler.generators import primes


def problem_seven():
    """Solution to problem seven."""
    counter = 0

    for prime in primes():
        counter += 1
        if counter == 10001:
            answer = prime
            break
    return answer

if __name__ == '__main__':
    print(problem_seven())
