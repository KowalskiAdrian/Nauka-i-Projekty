import unittest
from unittest.mock import patch
from io import StringIO

from interest_calculator import calculate_interest

class TestInterestCalculator(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1000', '5', '2'] + ['100', '200'] * 2)
    def test_calculate_interest(self, mock_input, mock_stdout):
        calculate_interest()
        expected_output = 'Wartość końcowa kapitału: 1310.25\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        print(f"Final value of capital: {calculate_interest}")


unittest.main()
