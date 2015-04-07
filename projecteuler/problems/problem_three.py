"""Problem three of https://github.com/heathy/project_euler"""

from math import sqrt
from itertools import takewhile
from projecteuler.generators import primes


NUMBER = 600851475143
prime_factors = [x for x in takewhile(lambda x: x < sqrt(NUMBER), primes())
                 if NUMBER % x == 0]
answer = prime_factors[-1]
print(answer)
