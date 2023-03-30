import pytest
from io import StringIO
from unittest.mock import patch

from interest_calculator import calculate_interest


class TestInterestCalculator:
    @pytest.mark.parametrize("inputs, expected_output", [
        (["1000", "5", "2", "100", "200", "100", "200"], "Wartość końcowa kapitału: 897.50\n"),  # updated expected output
        (["2000", "3", "1", "500", "750", "1000", "1500"], "Wartość końcowa kapitału: 1810.00\n")  # updated expected output
    ])
    def test_calculate_interest(self, inputs, expected_output):
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new=StringIO()) as mock_stdout:
            calculate_interest()
            assert mock_stdout.getvalue() == expected_output
