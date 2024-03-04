from mpmath import mp

def calculate_pi(digits):
    # Set precision for arithmetic calculations using mpmath
    mp.dps = digits + 2
    
    # Calculate pi with the desired precision and convert to a string
    pi_str = str(mp.pi)
    
    # Extract the portion of the string representing the desired number of decimal places
    result = pi_str[:2 + digits]
    
    return f"Pi to {digits} decimal places:\n{result}"

if __name__ == "__main__":
    while True:
        try:
            decimal_places = input("Enter the number of decimal places for π (type 'exit' to quit): ")

            if decimal_places.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            decimal_places = int(decimal_places)

            if 0 < decimal_places <= 1000:
                pi_result = calculate_pi(decimal_places)
                print(pi_result)
            else:
                print("Please enter a valid number of decimal places within the limit (1 to 1000).")

        except ValueError:
            print("Invalid input. Please enter a valid integer or 'exit'.")
