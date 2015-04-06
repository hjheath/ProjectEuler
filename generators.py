"""Generate sequences of numbers."""

from itertools import count


def fibonacci():
    """Fibonacci number generator."""
    second_last, last = 1, 1
    while True:
        yield last
        second_last, last = last, last + second_last


def prime():
    """
    Prime number generator.

    This uses the Sieve of Eratosthenes algorithim.
    """
    composite_numbers = {}
    yield 2

    for number in count(start=3, step=2):
        if number not in composite_numbers:
            composite_numbers[number*number] = number
            yield number

        else:
            highest_factor = composite_numbers[number]
            new_composite = number + highest_factor

            # We do not test even numbers so keep going to the next odd number.
            while new_composite in composite_numbers or new_composite % 2 == 0:
                new_composite += highest_factor
            composite_numbers[new_composite] = highest_factor
