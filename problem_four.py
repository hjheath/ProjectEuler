"""Problem four of https://github.com/heathy/project_euler"""

from inspectors import is_palindrome

ANSWER = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if is_palindrome(product) and product > ANSWER:
            ANSWER = product

print(ANSWER)
