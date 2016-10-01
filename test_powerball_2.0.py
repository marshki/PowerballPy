<<<<<<< HEAD
#!/usr/bin/env Python3 
""" 
Unit tests.
"""

# Import functions 

import unittest 
from powerball_2 import * 

# define testing class 

import unittest
import random

def white_nums(range_min, range_max, balls):
    return set(random.sample(range(range_min, range_max + 1), balls))


class TestWhiteNums(unittest.TestCase):

    def setUp(self):
        self.range_min = 1
        self.range_max = 69
        self.balls = 5
        self.white_balls = white_nums(self.range_min, self.range_max, self.balls)

    def test_count(self):
        self.assertEqual(len(self.white_balls), self.balls)

    def test_range(self):
        for white_ball in self.white_balls:
            self.assertGreaterEqual(white_ball, self.range_min)
            self.assertLessEqual(white_ball, self.range_max)

    def test_duplicates(self):
       self.assertEqual(self.white_balls, set(self.white_balls))

if __name__ == '__main__':
    unittest.main()


unittest.main()
=======
#!/usr/bin Python

# import Python module 
import unittest 
>>>>>>> 846964a2ab235b38418037d02720ad9a146c7619
