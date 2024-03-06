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

if __name__ == "__main__":
    while True:
        # Get user input
        user_input = input("Enter a number (type 'quit' to exit): ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            break
        
        try:
            # Convert input to an integer
            number = int(user_input)
            
            # Find prime factors and display them
            result = prime_factors(number)
            print(f"Prime factors of {number}: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'quit' to exit.")
