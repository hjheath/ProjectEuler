"""Test the problems get the correct answers."""

import unittest
import logging

# Using import * is acceptable here as the modules in the problems directory
# follow a strict naming convention. This works because __all__ is defined in
# problems.__init__.py to include all modules in the problems direcory.
from projecteuler.problems import *
from answers import PROBLEM_ANSWERS

logger = logging.getLogger(__name__)


class TestProblems(unittest.TestCase):
    """Test that each problem function returns the correct answer."""

    def check_answer(self, problem_name):
        """
        Check that that answer to the problem is correct.

        :param problem_name: A string of the module of the problem to check.
        """
        logger.info('Checking the answer to problem %s.', problem_name)
        # Use the module name to get the module from the global namespace.
        module = globals()[problem_name]
        # Conveninetly the problem function has the same name as the module.
        problem = getattr(module, problem_name)

        # The rest is then simple.
        answer = problem()
        logger.info('Answer calculated to %s: %d.', problem_name, answer)
        self.assertEqual(answer, PROBLEM_ANSWERS[problem_name])

    def test_answers(self):
        """Test the solution to all the problems."""
        for problem in PROBLEM_ANSWERS:
            self.check_answer(problem)


if __name__ == '__main__':
    unittest.main()
