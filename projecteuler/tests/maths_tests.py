"""Test maths functions."""

import unittest

import projecteuler.maths_functions as maths


class TestInspectors(unittest.TestCase):
    """Test that each inspector function works correctly."""

    def test_multiply(self):
        """Test multiplying all the elements of a list."""
        integers = [1, 2, 3]
        self.assertEqual(maths.multiply(integers), 6)

        floats = [1.0, 2.0, 3.0]
        self.assertEqual(maths.multiply(floats), 6.0)

        mixture = [1.0, 2, 0]
        self.assertEqual(maths.multiply(mixture), 0.0)

        singe_int = [1]
        self.assertEqual(maths.multiply(singe_int), 1)

        empty_list = []
        self.assertRaises(TypeError, maths.multiply, empty_list)

    def test_factor_count(self):
        """Test calculating the number of factors a number has."""
        self.assertEqual(maths.factor_count(1), 1)
        self.assertEqual(maths.factor_count(2), 2)
        self.assertEqual(maths.factor_count(10), 4)

        # Test a square number.
        self.assertEqual(maths.factor_count(9), 3)


if __name__ == '__main__':
    unittest.main()
