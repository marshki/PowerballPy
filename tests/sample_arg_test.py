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
