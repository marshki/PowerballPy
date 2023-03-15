#!/usr/bin/env python3

"""Testing class for 'make_table' function.
"""


import unittest
from prettytable import PrettyTable


def make_table():
    """Use 'PrettyTable' module to create table for output. Align left.
    """

    table = PrettyTable(['Whites #s', 'Red #'])
    table.align = 'l'
    return table


class TestMakeTable(unittest.TestCase):
    """Test class.
    """

    def test_make_table(self):
        """Test: table, field names, and alignment.
        """

        table = make_table()
        self.assertIsInstance(table, PrettyTable)
        self.assertEqual(table.field_names, ['Whites #s', 'Red #'])
        for field in table.field_names:
            self.assertEqual(table.align[field], 'l')


if __name__ == '__main__':
    unittest.main()
