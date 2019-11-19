#!/usr/bin/env python

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

    #@patch('builtins.input', return_value='n')
    #def test_numerical_input_02(self, input):
    #    """Valid return value.
    #    """
    #    self.assertEqual(numerical_input(), 'n')

if __name__ == '__main__':
    unittest.main()
