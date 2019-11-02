#!/usr/bin/env python

"""Psuedo-random number generator for Powerball lottery.
"""

import random
import unittest

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

if __name__ == '__main__':
    unittest.main()

unittest.main()
