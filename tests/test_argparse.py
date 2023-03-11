#!/usr/bin/env python3

"""Define sets of numbers to generate using argparse."""

import argparse

import unittest

def parse_cli_args():
    """Command line parser for user-defined sets of numbers.
    Args:
      --sets 10
    Returns:
        Integer, e.g. 10
    """

    parser = argparse.ArgumentParser(description="Set(s) of PowerBall numbers to generate.")
    parser.add_argument("--sets", action="store", type=int,\
                        required=False,\
                        help="Number of sets to generate, e.g. 10")

    return parser

class ParseCLIArgs(unittest.TestCase):

    """
    Unit tests.
    """
    def setUp(self):
        self.parser = parse_cli_args()

    def test_parser_cli_args_01(self):
        """Valid return value."""
        parsed = self.parser.parse_args(['--sets', '5'])
        self.assertEqual(parsed.sets, 5)

    def test_parser_cli_args_02(self):
        """Valid return value."""
        parsed = self.parser.parse_args(['--sets', '20'])
        self.assertEqual(parsed.sets, 20)

if __name__ == '__main__':
    unittest.main()
