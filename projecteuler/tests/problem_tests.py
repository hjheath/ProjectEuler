"""Test the problems get the correct answers."""

import unittest
import logging

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

        # Use __import__ as we only know the module we need at runtime.
        module_path = '.'.join(['projecteuler', 'problems', problem_name])

        # The fromlist must not be empty to obtain a reference to the module.
        module = __import__(module_path, fromlist=[None])

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
