import math

def basic_calculator():
    print("Basic Calculator")

    while True:
        try:
            num1 =  float(input('Enter first number: '))
            operator = input('Enter an operator (+, -, *, /, sqrt, sin, cos, tan, log, exp): ')

            if operator in ("+", "-", "*", "/"):
                num2 = float(input('Enter second number: '))

            if operator == "+":
                result = num1 + num2
            elif operator  == "-":
                result = num1 - num2
            elif operator   == "*":
                result = num1 * num2
            elif operator == "/":
                if num2==0:
                    print("Division by zero is not allowed.")
                    continue
                result = num1 / num2
            elif operator == "sqrt":
                result = math.sqrt(num1)
            elif operator == "sin":
                result = math.sin(math.radians(num1))
            elif operator == "cos":
                result = math.cos(math.radians(num1))
            elif operator == "tan":
                result = math.tan(math.radians(num1))
            elif  operator == "log":
                result = math.log10(num1)
            elif operator == "exp":
                result = math.exp(num1)
            else:
                print("Invalid Operator! Please try again.")
                continue

            print("Result", result)

            another_calculation = input("Do you want to perform another calculation?")
            if another_calculation.lower() != "yes":
                break

        except ValueError:
            print("Invalid Input! Please enter a valid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")


if __name__  == "__main__":
    basic_calculator()