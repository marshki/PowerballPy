#!/usr/bin/env python3
#pylint: disable=R0201

"""Unit tests for powerballyPy.py
"""

import unittest
from unittest.mock import patch
from prettytable import PrettyTable
from powerballpy import make_table
from powerballpy import white_numbers

class TestMakeTable(unittest.TestCase):
    """Test class.
    """

    def test_make_table(self):
        """Test: table, field names, and alignment.
        """

        table = make_table()
        self.assertIsInstance(table, PrettyTable)
        self.assertEqual(table.field_names, ['Whites #s', 'Red #'])
        for field in table.field_names:
            self.assertEqual(table.align[field], 'l')

class TestWhiteNumbers(unittest.TestCase):
    """Test class.
    """

    def setUp(self):
        self.range_min = 1
        self.range_max = 69
        self.balls = 5
        self.white_balls = white_numbers(self.range_min, self.range_max, self.balls)

    def test_count(self):
        """Test count of balls genertated.
        """
        self.assertEqual(len(self.white_balls), self.balls)

    def test_range(self):
        """Test white_ball falls within min and max range.
        """
        for white_ball in self.white_balls:
            self.assertGreaterEqual(white_ball, self.range_min)
            self.assertLessEqual(white_ball, self.range_max)

    def test_duplicates(self):
        """Test for white_ball duplicates.
        """
        self.assertEqual(self.white_balls, set(self.white_balls))

if __name__ == '__main__':
    unittest.main()
