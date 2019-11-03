#!/usr/bin/env python

"""Unit tests for powerball.py
"""

from __future__ import print_function
from builtins import input

import unittest

from unittest.mock import patch

def yes_no_input():
    """Prompt user for Y/N input.
    """

    while True:
        try:
            user_input = str(input('Generate Powerball numbers? Y/N: ')).lower()
            if user_input in ['y', 'n']:
                return user_input
        except ValueError:
            print('Try again')

class YesNoInput(unittest.TestCase):

    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='y')
    def test_yes_no_input_01(self, input):
        """Valid return value.
        """
        self.assertEqual(yes_no_input(), user_input)

if __name__ == '__main__':
    unittest.main()
