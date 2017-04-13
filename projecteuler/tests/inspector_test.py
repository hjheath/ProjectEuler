"""Test the functions used to inspect a number."""

import unittest

import projecteuler.inspectors as inspectors


class TestInspectors(unittest.TestCase):
    """Test that each inspector function works correctly."""

    def test_is_palindrome(self):
        """Test detecting palindromes."""
        # Test an odd number of digits.
        self.assertTrue(inspectors.is_palindrome(12321))
        self.assertTrue(inspectors.is_palindrome(1))
        self.assertFalse(inspectors.is_palindrome(19321))

        # Test an even number of digits.
        self.assertTrue(inspectors.is_palindrome(312213))
        self.assertFalse(inspectors.is_palindrome(23))

    def test_is_prime(self):
        """Test detecing primes."""
        self.assertFalse(inspectors.is_prime(1))
        self.assertTrue(inspectors.is_prime(2))
        self.assertTrue(inspectors.is_prime(983))

        # Test a square number.
        self.assertFalse(inspectors.is_prime(9))

        # Test a negative number.
        self.assertFalse(inspectors.is_prime(-7))

    def test_is_pandigital(self):
        """Test detecting pandigitals"""
        self.assertTrue(inspectors.is_pandigital('123456789'))
        self.assertFalse(inspectors.is_pandigital('12345678'))
        self.assertFalse(inspectors.is_pandigital('012345678'))
        self.assertFalse(inspectors.is_pandigital('1234567899'))

        result = inspectors.is_pandigital('1234567890', include_zero=True)
        self.assertTrue(result)

        result = inspectors.is_pandigital('123456789', include_zero=True)
        self.assertFalse(result)

    def test_pandigital_product(self):
        """Test detecting pandigital products."""
        # A product with duplicate digits.
        self.assertFalse(inspectors.pandigital_product(1269, 46))
        # A product containing a zero.
        self.assertFalse(inspectors.pandigital_product(39, 1860))
        # A pandigital product.
        self.assertEqual(inspectors.pandigital_product(39, 186), 7254)

    def test_curious_fractions(self):
        """Test detecting curious fractions."""
        self.assertTrue(inspectors.is_curious_fraction(49, 98))
        self.assertFalse(inspectors.is_curious_fraction(23, 32))

        # Test the trivial case is False.
        self.assertFalse(inspectors.is_curious_fraction(30, 50))
