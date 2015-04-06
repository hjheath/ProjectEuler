"""Problem three of https://github.com/heathy/project_euler"""

from math import sqrt
from itertools import takewhile
from generators import prime


NUMBER = 600851475143
PRIME_FACTORS = [x for x in takewhile(lambda x: x < sqrt(NUMBER), prime())
                 if NUMBER % x == 0]
ANSWER = PRIME_FACTORS[-1]
print(ANSWER)
