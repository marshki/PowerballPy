import unittest
import argparse
import sys
from io import StringIO

class TestArgParse(unittest.TestCase):
        
    def test_default_num_sets(self):
        parser = argparse.ArgumentParser()
        args = parser.parse_args([])
        self.assertEqual(args.num_sets, 1)


