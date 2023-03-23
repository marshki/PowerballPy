#!/usr/bin/env python3
#pylint: disable=R0201

"""Unit tests for powerballyPy.py
"""

import unittest
# from unittest.mock import patch
from prettytable import PrettyTable
from powerballpy import make_table
from powerballpy import white_numbers

class TestMakeTable(unittest.TestCase):
    """Test class.
    """

    def test_make_table(self):
        """Test table creation; table field names; and table alignment.
        """

        table = make_table()
        self.assertIsInstance(table, PrettyTable)
        self.assertEqual(table.field_names, ['Whites #s', 'Red #'])
        for field in table.field_names:
            self.assertEqual(table.align[field], 'l')

class TestWhiteNumbers(unittest.TestCase):
    """Test class.
    """

    def test_output_is_list(self):
        """Test if instance is list.
        """

        result = white_numbers()
        self.assertIsInstance(result, list)

    def test_output_has_five_elements(self):
        """Test if set contains five elements.
        """

        result = white_numbers()
        self.assertEqual(len(result), 5)

    def test_output_has_unique_elements(self):
        """Test if elements of set are unique.
        """

        result = white_numbers()
        self.assertEqual(len(set(result)), 5)

    def test_output_has_integers_between_1_and_69(self):
        """Test if elements of list are between 1 and 69, inclusive.
        """

        result = white_numbers()
        self.assertTrue(all(1 <= n <= 69 for n in result))

    
class TestRedNumber(unittest.TestCase):
    """Test class.
    """    

    def test_output_is_int(self):
        result = red_number()
        self.assertIsInstance(result, int)
    
    def test_output_is_between_1_and_26(self):
        result = red_number()
        self.assertTrue(1 <= result <= 26)

if __name__ == '__main__':
    unittest.main()
