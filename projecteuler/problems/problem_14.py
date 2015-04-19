"""Problem 14 of https://projecteuler.net"""

from projecteuler.generators import next_collatz


def problem_14():
    """Solution to problem 14."""
    calculator = CollatzCalculator()
    # Get the number below 1,000,000 that has the maximum collatz count.
    answer = (max(range(1, 1000000), key=calculator.collatz_count))
    return answer


class CollatzCalculator:
    """A class to calculate the collatz count of a number."""

    def __init__(self):
        # Initialise the count cache - the collatz count for one is one.
        self.count_cache = {1: 1}

    def collatz_count(self, number):
        """
        Get the number of terms in a collatz sequence terminating at 1.

        :param number: The starting number in the collatz sequence.

        :returns: The collatz count of the number.
        """
        if number not in self.count_cache:
            next_number = next_collatz(number)
            # Use recursion until we find a number that is not in the cache.
            count = self.collatz_count(next_number) + 1
            self.count_cache[number] = count
        else:
            count = self.count_cache[number]
        return count


if __name__ == '__main__':
    print(problem_14())
