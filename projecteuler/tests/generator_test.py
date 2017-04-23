"""Test the functions used to generate sequences."""

import unittest
from itertools import takewhile

import projecteuler.generators as generators

FIBONACCIS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
TRIANGLES = [1, 3, 6, 10, 15, 21, 28, 36, 45]
PENTAGONS = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]


class TestGenerators(unittest.TestCase):
    """Test that each generator function returns the correct sequence."""

    def test_fibonacci(self):
        """Test the fibonnaci generator function."""
        fibonaccis = [x for x in takewhile(lambda x: x < 100,
                                           generators.fibonaccis())]
        self.assertEqual(fibonaccis, FIBONACCIS)

    def test_primes(self):
        """Test the prime generator function."""
        primes = [x for x in takewhile(lambda x: x < 50, generators.primes())]
        self.assertEqual(primes, PRIMES)

    def test_prime_factors(self):
        """Test calculating the prime factors of a number."""
        # 100 has duplicate primes and different primes.
        factors_100 = [2, 2, 5, 5]
        factors = [x for x in generators.prime_factors(100)]
        self.assertEqual(factors, factors_100)

        # Test a prime number.
        factors_19 = [19]
        factors = [x for x in generators.prime_factors(19)]
        self.assertEqual(factors, factors_19)

        # 1 does not have any prime factors.
        factors_1 = []
        factors = [x for x in generators.prime_factors(1)]
        self.assertEqual(factors, factors_1)

    def test_triangle_numbers(self):
        """Test the triangle number generator function."""
        generator = generators.triangle_numbers()
        triangles = [x for x in takewhile(lambda x: x < 50, generator)]
        self.assertEqual(triangles, TRIANGLES)

    def test_pentagon_numbers(self):
        """Test the pentagon number generator function."""
        generator = generators.pentagon_numbers()
        pentagons = [x for x in takewhile(lambda x: x < 150, generator)]
        self.assertEqual(pentagons, PENTAGONS)

    def test_next_collatz(self):
        """Test the function to get the next number in a collatz sequence."""
        # Test an even number.
        collatz_10 = 5
        next_collatz = generators.next_collatz(10)
        self.assertEqual(next_collatz, collatz_10)

        # Test an odd number.
        collatz_7 = 22
        next_collatz = generators.next_collatz(7)
        self.assertEqual(next_collatz, collatz_7)

    def test_pythagorean_triples(self):
        """Test the Pythagorean triple generator"""
        triples = [x for x in generators.pythagorean_triples(5)]
        self.assertEqual(triples, [(3, 4, 5)])

        triples = [x for x in generators.pythagorean_triples(13)]
        self.assertTrue((5, 12, 13) in triples)
        self.assertTrue(len(triples) == 3)

        triples = [x for x in generators.pythagorean_triples(0)]
        self.assertEqual(triples, [])
