#!/usr/bin/env python
# pylint: disable=W0613,W0622

"""Unit test for powerball.py.
"""

import unittest

from unittest.mock import patch

def numerical_input():
    """Prompt user for numerical input.
    """

    while True:
        try:
            return int(input('How many sets of Powerball numbers should we generate?: '))
        except ValueError:
            print('Try again')
            raise

class NumericalInput(unittest.TestCase):

    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='10')
    def test_numerical_input_01(self, input):
        """Valid return value.
        """
        self.assertIsInstance(numerical_input(), int)

    @patch('builtins.input', return_value='Derp!')
    def test_numerical_input_02(self, input):
        """Invalid return value.
        """
        with self.assertRaises(ValueError):
            numerical_input()

if __name__ == '__main__':
    unittest.main()
