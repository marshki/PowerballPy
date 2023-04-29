#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Powerball Number Generator")
parser.add_argument("-n", "--num_sets", type=int, default=1, help="Number of sets to generate")

args = parser.parse_args()

try:
    if args.num_sets < 1:
        raise argparse.ArgumentTypeError("Number of sets must be a positive integer.")
except argparse.ArgumentTypeError as e:
    parser.error(str(e))

"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import argparse

from powerball import main

class TestPowerball(unittest.TestCase):
    def test_negative_num_sets(self):
        with patch('sys.stderr', new=StringIO()) as error_output:
            with self.assertRaises(SystemExit):
                parser = argparse.ArgumentParser()
                parser.add_argument("-n", "--num_sets", type=int, default=1, help="Number of sets to generate")
                args = parser.parse_args(['-n', '-1'])
                main(args)

        self.assertEqual(error_output.getvalue().strip(), 'usage: powerball.py [-h] [-n NUM_SETS]\n'
                                                          'powerball.py: error: argument -n/--num_sets: Number of sets must be a positive integer.')
"""
