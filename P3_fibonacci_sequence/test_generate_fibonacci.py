

##### not done ####


import unittest
from generate_fibonacci import fibSequence

class TestFibonacciSequence(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(fibSequence(1), '1')
        self.assertEqual(fibSequence(5), '1, 1, 2, 3, 5')
        self.assertEqual(fibSequence(10), '1, 1, 2, 3, 5, 8, 13, 21, 34, 55')

    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            fibSequence(0)
        with self.assertRaises(ValueError):
            fibSequence(-5)

if __name__ == '__main__':
    unittest.main()
