#!/usr/bin/env python3

import unittest
from prettytable import PrettyTable


def make_table():
    """Use 'PrettyTable' module to create table for output. Align left.
    """

    table = PrettyTable(['Whites #s', 'Red #'])
    table.align = 'l'
    return table


class TestMakeTable(unittest.TestCase):

    def test_make_table(self):
        table = make_table()
        self.assertIsInstance(table, PrettyTable)
        self.assertEqual(table.field_names, ['Whites #s', 'Red #'])
        self.assertEqual(table.align, 'l')

if __name__ == '__main__':
    unittest.main()
