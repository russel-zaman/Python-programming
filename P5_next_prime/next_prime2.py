"""
Find the next prime number until the user chooses to stop asking for the next one
"""
from math import sqrt

def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for divisor in range(3, int(sqrt(number)+1), 2):
            if number % divisor == 0:
                return False
        return True
    return False

def gen_primes():
    yield 2
    number = 3
    while True:
        if isPrime(number):
            yield number
        number += 2

def main():
    print("Press Enter to generate next prime number, 's' to stop.")
    generator = gen_primes()
    while True:
        ans = input()

        if ans == 's':
            break
        else:
            print(next(generator))

if __name__ == '__main__':
    main()
