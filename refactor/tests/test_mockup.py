#!/usr/bin/env python3
#pylint: disable=R0201

"""Unit tests for powerballyPy.py
"""

import argparse
import random
import unittest
from unittest.mock import patch
from prettytable import PrettyTable
from powerballpy import main

def make_table():
    """Use 'PrettyTable' module to create table for output. Align left.
    """

    table = PrettyTable(['Whites #s', 'Red #'])
    table.align = 'l'
    return table

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

def white_numbers(range_min, range_max, balls):
    """Generate n pseudo-random numbers between min and max range +1.
    """
    return set(random.sample(range(range_min, range_max + 1), balls))

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

def red_number(range_min, range_max, balls):
    """Generate n pseudo-random number between min and max range +1.
    """
    return set(random.sample(range(range_min, range_max + 1), balls))

class TestRedNumber(unittest.TestCase):
    """Test class.
    """

    def setUp(self):
        self.range_min = 1
        self.range_max = 26
        self.ball = 1
        self.red_ball = red_number(self.range_min, self.range_max, self.ball)

    def test_count(self):
        """Test count of ball generated.
        """
        self.assertEqual(len(self.red_ball), self.ball)

    def test_range(self):
        """"Test red ball falls within min and max range.
        """
        for red_ball in self.red_ball:
            self.assertGreaterEqual(red_ball, self.range_min)
            self.assertLessEqual(red_ball, self.range_max)

class TestArgParsing(unittest.TestCase):
    """Test class.
    """

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(num_sets=3))
    def test_num_sets_arg(self, mock_args):
        """Test argument parsing.
        """
        main()
        mock_args.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
