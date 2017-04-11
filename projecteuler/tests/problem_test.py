"""Test the problems get the correct answers."""

import unittest

from projecteuler.tests.answers import PROBLEM_ANSWERS


class MetaTests(type):
    """Meta class to dynamically create test cases for each problem"""
    def __new__(mcs, name, bases, attrs):
        for problem_name, answer in PROBLEM_ANSWERS.items():
            # Use __import__ as we only know the module we need at runtime.
            module_path = '.'.join(['projecteuler', 'problems', problem_name])

            # The fromlist must not be empty.
            module = __import__(module_path, fromlist=[None])

            # The problem function has the same name as the module.
            problem = getattr(module, problem_name)
            attrs['test_' + problem_name] = mcs.generate_test(problem, answer)

        return super().__new__(mcs, name, bases, attrs)

    @classmethod
    def generate_test(mcs, problem, answer):
        """Dynamically generate a test method"""
        def test_function(self):
            """The actual test."""
            self.assertEqual(problem(), answer)
        return test_function


class TestProblems(unittest.TestCase, metaclass=MetaTests):
    """Test that each problem function returns the correct answer."""
