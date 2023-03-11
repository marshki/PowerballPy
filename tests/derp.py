#!/usr/bin/env python3

"""Define sets of numbers to generate using argparse."""

import argparse
import unittest
from argparse import Namespace
from parse_cli_args import parse_cli_args

def parse_cli_args():
    """Command line parser for user-defined sets of numbers.
    Args:
        --sets 10
    Returns:
        Integer, e.g. 10
    """

    parser = argparse.ArgumentParser(description="Set(s) of PowerBall numbers to generate.")
    parser.add_argument("--sets", action="store", type=int, required=False, help="Number of sets to generate, e.g. 10")

    args = parser.parse_args()

    return args.sets

class TestParseCliArgs(unittest.TestCase):

    def test_no_sets(self):
        """Test the function when no sets are specified"""
        args = Namespace(sets=None)
        self.assertIsNone(parse_cli_args(args))

    def test_valid_sets(self):
        """Test the function when valid sets are specified"""
        args = Namespace(sets=10)
        self.assertEqual(parse_cli_args(args), 10)

    def test_invalid_sets(self):
        """Test the function when an invalid value is specified for sets"""
        args = Namespace(sets="abc")
        with self.assertRaises(SystemExit):
            parse_cli_args(args)

if __name__ == '__main__':
    unittest.main()
