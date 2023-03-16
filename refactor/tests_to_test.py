import unittest
import io
from unittest.mock import patch
from powerball import generate_powerball_table


class TestPowerball(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    def test_numerical_input(self, mock_input):
        self.assertEqual(numerical_input(), 3)

    def test_white_numbers(self):
        for i in range(100):
            whites = white_numbers()
            self.assertEqual(len(whites), 5)
            self.assertEqual(min(whites), 1)
            self.assertEqual(max(whites), 69)
            self.assertEqual(len(set(whites)), 5)

    def test_red_number(self):
        for i in range(100):
            red = red_number()
            self.assertEqual(len(red), 1)
            self.assertEqual(min(red), 1)
            self.assertEqual(max(red), 26)

    def test_generate_powerball_table(self):
        table = generate_powerball_table(3)
        self.assertEqual(len(table._rows), 3)
        for row in table._rows:
            self.assertEqual(len(row), 2)
            self.assertEqual(len(row[0].split(', ')), 5)
            self.assertEqual(len(row[1].split(', ')), 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_argument_parsing_default(self, mock_stdout):
        with patch('sys.argv', ['powerball.py']):
            generate_powerball_table(1)
            self.assertEqual(mock_stdout.getvalue(), '+-----------+-------+\n| Whites #s | Red # |\n+-----------+-------+\n| 9, 56, 12, 59, 53 | 3     |\n+-----------+-------+\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_argument_parsing_num_sets(self, mock_stdout):
        with patch('sys.argv', ['powerball.py', '-n', '2']):
            generate_powerball_table(2)
            self.assertEqual(mock_stdout.getvalue(), '+-----------+-------+\n| Whites #s | Red # |\n+-----------+-------+\n| 58, 11, 14, 45, 25 | 21    |\n| 29, 50, 48, 23, 33 | 19    |\n+-----------+-------+\n')

if __name__ == '__main__':
    unittest.main()
