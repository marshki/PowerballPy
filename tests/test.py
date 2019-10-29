#!/usr/bin/env Python3
"""
Unit tests.
"""

import random
import unittest
from powerball import *

# Define testing class

def white_numbers(range_min, range_max, balls):
    return set(random.sample(range(range_min, range_max + 1), balls))


class TestWhiteNumbers(unittest.TestCase):

    def setUp(self):
        self.range_min = 1
        self.range_max = 69
        self.balls = 5
        self.white_balls = white_numbers(self.range_min, self.range_max, self.balls)

    def test_count(self):
        self.assertEqual(len(self.white_balls), self.balls)

    def test_range(self):
        for white_ball in self.white_balls:
            self.assertGreaterEqual(white_ball, self.range_min)
            self.assertLessEqual(white_ball, self.range_max)

    def test_duplicates(self):
        self.assertEqual(self.white_balls, set(self.white_balls))

def red_number(range_min, range_max, balls):
    return set(random.sample(range(range_min, range_max + 1), balls))

class TestRedNumber(unittest.TestCase):

    def setUp(self):
        self.range_min = 1
        self.range_max = 26
        self.ball = 1
        self.red_ball = red_number(self.range_min, self.range_max, self.ball)

    def test_count(self):
        self.assertEqual(len(self.red_ball), self.ball)

    def test_range(self):
        for red_ball in self.red_ball:
            self.assertGreaterEqual(red_ball, self.range_min)
            self.assertLessEqual(red_ball, self.range_max)

    #def test_duplicates(self):
    #   self.assertEqual(self.white_balls, set(self.white_balls))

if __name__ == '__main__':
    unittest.main()

unittest.main()
