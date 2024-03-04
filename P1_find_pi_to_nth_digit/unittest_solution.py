##### not solved  yet ####

import unittest
from find_pi_to_nth_digit import calculate_pi

class TestCalculatePi(unittest.TestCase):
    def test_calculate_pi(self):
        # Test 10 decimal places
        self.assertEqual(calculate_pi(10), "Pi to 10 decimal places:\n3.1415926535")

        # Test 50 decimal places
        self.assertEqual(calculate_pi(50), "Pi to 50 decimal places:\n3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068")

        # Test invalid input
        with self.assertRaises(ValueError):
            calculate_pi(-1)

        with self.assertRaises(ValueError):
            calculate_pi(0)

        with self.assertRaises(ValueError):
            calculate_pi(1001)

        # Test exit condition
        with self.assertLogs('calculate_pi', level='INFO') as cm:
            calculate_pi('exit')
            self.assertEqual(cm.output, ['Exiting the program. Goodbye!'])

if __name__ == '__main__':
    unittest.main()