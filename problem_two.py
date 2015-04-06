"""Problem two of https://github.com/heathy/project_euler"""

from itertools import takewhile
from generators import fibonacci

FIBONACCI_NUMBERS = [x for x in takewhile(lambda x: x < 4000000, fibonacci())]
ANSWER = sum(y for y in FIBONACCI_NUMBERS if y % 2 == 0)

print(ANSWER)
