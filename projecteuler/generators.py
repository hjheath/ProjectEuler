"""Functions to generate sequences of numbers."""

from itertools import count


def fibonaccis():
    """Fibonacci number generator."""
    second_last, last = 1, 1
    while True:
        yield second_last
        second_last, last = last, last + second_last


def primes():
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


def prime_factors(number):
    """
    Prime factor generator.

    :param number: An int for which we get the prime factors.
    """
    maximum = number
    for prime in primes():
        if prime > maximum:
            break
        while number % prime == 0:
            yield prime
            number = number / prime
            if number == 1:
                break


def triangle_numbers():
    """
    Triangle number generator.

    The nth triangle number is the sum of the first n numbers.
    """
    number = 1
    while True:
        yield int(number * (number + 1) / 2)
        number += 1


def pentagon_numbers():
    """
    Pentagon number generator

    Use the formula: n(3n−1)/2
    """
    number = 1
    while True:
        yield int(number * (3 * number - 1) / 2)
        number += 1


def next_collatz(number):
    """
    Get the next number in a collatz series.

    :param number: The previous number in the collatz series.

    :returns: The next number in the collatz series.
    """
    if number % 2 == 0:
        number = number // 2
    else:
        number = (3 * number) + 1
    return number


def pythagorean_triples(limit):
    """Pythagorean triple generator."""
    for x in range(1, limit):
        x_squared = x * x
        y = x + 1
        z = y + 1
        while z <= limit:
            expected_z_squared = x_squared + y * y
            while z * z < expected_z_squared:
                z += 1
            if z * z == expected_z_squared and z <= limit:
                yield (x, y, z)
            y += 1
