def generate_fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]

def get_user_input():
    try:
        user_input = int(input("Enter the number or Nth term for Fibonacci sequence (enter 0 to exit): "))
        if user_input < 0:
            raise ValueError("Please enter a non-negative integer.")
        return user_input
    except ValueError as e:
        print(f"Error: {e}")
        return get_user_input()

def main():
    while True:
        user_input = get_user_input()

        if user_input == 0:
            print("Exiting the program.")
            break

        # Generate and print the Fibonacci sequence
        result = generate_fibonacci(user_input)
        print(f"Fibonacci sequence up to {user_input}: {result}")

if __name__ == '__main__':
    main()
