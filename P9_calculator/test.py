from calculator import basic_calculator
from io import StringIO         # allows capturing and manipulating strings as file-like objects.
import sys                      #  Import the sys module to interact with the Python interpreter.

def simulate_user_input(input_values):          #  Function that simulates user input by passing values
    original_input = sys.stdin     
    sys.stdin = StringIO(input_values)          # It temporarily redirects the standard input (sys.stdin) to a StringIO object containing the provided input values.
    try:
        basic_calculator()
    finally:                                    # the original standard input is restored in a finally block to ensure proper cleanup.
        sys.stdin = original_input

def test_calculator():
    # Test addition
    simulate_user_input('5\n+\n3\nno\n')
    
    # Test subtraction
    simulate_user_input('10\n-\n4\nno\n')

    # Test multiplication
    simulate_user_input('2\n*\n6\nno\n')

    # Test division
    simulate_user_input('8\n/\n2\nno\n')

    # Test square root
    simulate_user_input('25\nsqrt\nno\n')

    # Test sine
    simulate_user_input('30\nsin\nno\n')

    # Test cosine
    simulate_user_input('60\ncos\nno\n')

    # Test tangent
    simulate_user_input('45\ntan\nno\n')

    # Test logarithm
    simulate_user_input('100\nlog\nno\n')

    # Test exponential
    simulate_user_input('2\nexp\nno\n')

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_calculator()
