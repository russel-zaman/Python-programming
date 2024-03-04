#### not done :( ###
### not working ###


import unittest
from unittest.mock import patch
from find_e_to_nth_digit import calculate_e

class TestCalculateE(unittest.TestCase):

    @patch("builtins.input", side_effect=["5", "exit"])
    def test_calculate_e_with_valid_input(self, mock_input):
        expected_output = "Euler's number rounded to 5 decimal places: 2.71828"

        with patch("sys.stdout") as mock_stdout:
            calculate_e.main()

        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    @patch("builtins.input", side_effect=["non-integer", "3", "exit"])
    def test_calculate_e_with_invalid_input(self, mock_input):
        expected_output = "Invalid input. Please enter an integer or 'exit.'"

        with patch("sys.stdout") as mock_stdout:
            calculate_e.main()

        actual_output = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
