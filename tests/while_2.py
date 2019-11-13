#!/bin/python

import unittest

from unittest.mock import patch
from unittest import TestCase

def yes_no_input():
    while True:
        user_input = str(input('Generate Powerball numbers? Y/N:  ')).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input

class YesNoInput(unittest.TestCase):

    def get_input(self):
        return input(self)

    @patch('builtins.input', return_value='y')
    def test_yes_no_input_01(self, input):
        self.assertEqual(yes_no_input(), 'y')

    @patch('builtins.input', return_value='n')
    def test_yes_no_input_02(self, input):
        self.assertEqual(yes_no_input(), 'n')

if __name__ == '__main__':
    unittest.main()
