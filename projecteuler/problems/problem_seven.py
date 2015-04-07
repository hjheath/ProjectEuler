"""Problem seven of https://github.com/heathy/project_euler"""

from projecteuler.generators import primes

counter = 0

for prime in primes():
    counter += 1
    if counter == 10001:
        answer = prime
        break

print(answer)
