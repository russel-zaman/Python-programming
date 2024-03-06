
############ not working ##########



import unittest
from unittest.mock import patch, Mock
from io import StringIO

def factors(n):
    return [x for x in range(1, n+1) if not n % x]

is_prime = lambda n: len(factors(n)) == 2

primefactors = lambda n: list(filter(is_prime, factors(n)))

def primeFactorize(n):
    n = int(n)
    f = primefactors(n)
    
    # If the number is 1, return '1' directly
    if n == 1:
        return '1'
    
    # If the number is prime, return its string representation
    elif is_prime(n):
        return str(n)
    
    else:
        # Return the first prime factor followed by "*" and the factorization of the remaining part
        return str(f[0]) + "*" + primeFactorize(n // f[0])


class TestPrimeFactorization(unittest.TestCase):
    
    def test_factors(self):
        self.assertEqual(factors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(factors(17), [1, 17])
    
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))
    
    def test_primefactors(self):
        self.assertEqual(primefactors(24), [2, 3])
        self.assertEqual(primefactors(37), [37])
    
    def test_primeFactorize(self):
        self.assertEqual(primeFactorize(18), '2*3*3')
        self.assertEqual(primeFactorize(23), '23')
        self.assertEqual(primeFactorize(1), '1')
    
    @patch('builtins.input', side_effect=['12', '23', 'quit'])
    @patch('sys.exit', Mock())
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_program(self, mock_stdout, mock_exit, mock_input):
        with patch('sys.argv', ['script.py']):
            exec(open('script.py').read())
        
        mock_exit.assert_called_once_with(0)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Welcome to the Prime Factorizer. Enter the numbers in the prompt or enter \'quit\' to exit\n2*2*3\n23')

if __name__ == '__main__':
    unittest.main()