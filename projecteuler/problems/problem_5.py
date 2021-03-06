"""Problem five of https://projecteuler.net"""

from projecteuler.generators import prime_factors
from collections import Counter
from projecteuler.maths_functions import multiply


def problem_5():
    """Solution to problem five."""
    highest_count = {}
    for number in range(1, 21):
        factors = [factor for factor in prime_factors(number)]
        factor_count = Counter(factors)

        for factor in factor_count:
            if factor not in highest_count:
                highest_count[factor] = factor_count[factor]
            elif factor_count[factor] > highest_count[factor]:
                highest_count[factor] = factor_count[factor]

    factors = [factor ** highest_count[factor] for factor in highest_count]

    # This multiplies together the elements of the list.
    answer = multiply(factors)
    return answer
