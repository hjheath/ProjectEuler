"""Problem 39 of https://projecteuler.net"""

from projecteuler.generators import pythagorean_triples


def problem_39():
    """Solution to problem 39."""
    triples = pythagorean_triples(1000)
    perimeters = map(sum, triples)
    perimeters = list(filter(lambda x: x < 1000, perimeters))
    return max(set(perimeters), key=perimeters.count)


if __name__ == '__main__':
    print(problem_39())
