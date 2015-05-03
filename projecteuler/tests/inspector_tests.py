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

    def test_pandigital_product(self):
        """Test detecting pandigital products."""
        # A product with duplicate digits.
        self.assertFalse(inspectors.pandigital_product(1269, 46))
        # A product containing a zero.
        self.assertFalse(inspectors.pandigital_product(39, 1860))
        # A pandigital product.
        self.assertEqual(inspectors.pandigital_product(39, 186), 7254)


if __name__ == '__main__':
    unittest.main()
