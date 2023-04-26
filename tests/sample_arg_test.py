import unittest
import argparse
import sys
from io import StringIO

class TestArgParse(unittest.TestCase):
        
    def test_default_num_sets(self):
        parser = argparse.ArgumentParser()
        args = parser.parse_args([])
        self.assertEqual(args.num_sets, 1)

    def test_custom_num_sets(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--num_sets", type=int, default=1)
        args = parser.parse_args(['-n', '5'])
        self.assertEqual(args.num_sets, 5)

    def test_invalid_num_sets(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--num_sets", type=int, default=1)
        with self.assertRaises(SystemExit):
            parser.parse_args(['-n', 'foo'])

    def test_other_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--filename", type=str, default="output.txt")
        args = parser.parse_args(['-f', 'results.txt'])
        self.assertEqual(args.filename, 'results.txt')


