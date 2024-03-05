
##### not done yet #######


import unittest
from unittest.mock import patch
from io import StringIO
from generate_fib2 import generate_fibonacci, get_user_input

class TestFibonacciProgram(unittest.TestCase):

    def test_generate_fibonacci(self):
        self.assertEqual(generate_fibonacci(0), [])
        self.assertEqual(generate_fibonacci(1), [0])
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])

    @patch('builtins.input', side_effect=['5'])
    def test_get_user_input_valid(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_input = get_user_input()
            self.assertEqual(user_input, 5)

        output = mock_stdout.getvalue().strip()
        self.assertNotEqual(output, "")  # Ensure that there is some output

    @patch('builtins.input', side_effect=['abc', '-3', '6'])
    def test_get_user_input_invalid_then_valid(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_input = get_user_input()
            self.assertEqual(user_input, 6)

        output = mock_stdout.getvalue().strip()
        self.assertNotEqual(output, "")  # Ensure that there is some output

if __name__ == '__main__':
    unittest.main()
