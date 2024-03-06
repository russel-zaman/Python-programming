
########## working code ##########


import unittest

def prime_factors(n):
    factors = []
    divisor = 2
    
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    return factors

class TestPrimeFactors(unittest.TestCase):
    
    def test_prime_factors(self):
        # Test cases with expected prime factors
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(45), [3, 3, 5])
        self.assertEqual(prime_factors(97), [97])
    
    def test_prime_factors_edge_cases(self):
        # Test cases for edge values
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(0), [])
        self.assertEqual(prime_factors(99), [3, 3, 11])

if __name__ == '__main__':
    unittest.main()
