# Lambda function to find factors of a number
factors = lambda n: [x for x in range(1, n+1) if not n % x]

# regular expression
# def factors(n):
#     factor_list = []
#     for x in range(1, n+1):
#         if not n % x:
#             factor_list.append(x)
#     return factor_list


# Lambda function to check if a number is prime
is_prime = lambda n: len(factors(n)) == 2

# regular expression
# def is_prime_regular(n):
#     return len(factors(n)) == 2

# Lambda function to filter prime factors from the list of factors
primefactors = lambda n: list(filter(is_prime, factors(n)))

# regular expression
# def primefactors_regular(n):
#     return list(filter(is_prime_regular, factors(n)))


# Function to perform prime factorization recursively
def primeFactorize(n):
    n = int(n)
    f = primefactors(n)
    
    # If the number is prime, return its string representation
    if is_prime(n):
        return str(n)
    else:
        # Return the first prime factor followed by "*" and the factorization of the remaining part
        return str(f[0]) + "*" + primeFactorize(n / f[0])

# Main program execution
if __name__ == '__main__':
    print("Welcome to the Prime Factorizer. Enter the numbers in the prompt or enter 'quit' to exit")
    num = 0

    while True:
        if num:
            print(primeFactorize(num))
        print(">>>", end='')
        num = input()
        if num == "quit":
            break
