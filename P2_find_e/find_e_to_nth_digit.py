from decimal import Decimal, getcontext
import math

def calculate_e(round_val):
    getcontext().prec = round_val + 2  # Set precision to desired decimal places + 2
    some_e = Decimal(math.e)
    return round(some_e, round_val)

def main():
    while True:
        round_to = input('Enter the number of digits you want after the decimal for e (type "exit" to quit): ')

        if round_to.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        try:
            round_int = int(round_to)
            result = calculate_e(round_int)
            print(f"Euler's number rounded to {round_int} decimal places: {result}")
        except ValueError:
            print("Invalid input. Please enter an integer or 'exit.'")

if __name__ == '__main__':
    main()
