import unittest
from bin_to_dec_bin import decimal_to_binary, binary_to_decimal

class TestConverterFunctions(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(25), '11001')
        # Add more test cases as needed

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('1010'), 10)
        self.assertEqual(binary_to_decimal('11001'), 25)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
