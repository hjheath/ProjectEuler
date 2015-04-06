"""Problem five of https://github.com/heathy/project_euler"""

from generators import prime_factors
from collections import Counter
from functools import reduce


HIGHEST_COUNT = {}
for number in range(1, 21):
    factors = [factor for factor in prime_factors(number)]
    factor_count = Counter(factors)

    for factor in factor_count:
        if factor not in HIGHEST_COUNT:
            HIGHEST_COUNT[factor] = factor_count[factor]
        elif factor_count[factor] > HIGHEST_COUNT[factor]:
            HIGHEST_COUNT[factor] = factor_count[factor]

FACTORS = [factor ** HIGHEST_COUNT[factor] for factor in HIGHEST_COUNT]

# This multiplies together the elements of the list.
ANSWER = reduce(lambda x, y: x * y, FACTORS)

print(ANSWER)
