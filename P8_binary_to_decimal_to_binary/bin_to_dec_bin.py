def decimal_to_binary(decimal_number):
    return bin(decimal_number).replace("0b", "")

def binary_to_decimal(binary_number):
    return int(binary_number, 2)

def main():
    while True:
        print("Choose conversion type:")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            decimal_number = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(decimal_number)
            print(f"The binary equivalent of {decimal_number} is: {binary_result}\n")
        elif choice == '2':
            binary_number = input("Enter a binary number: ")
            decimal_result = binary_to_decimal(binary_number)
            print(f"The decimal equivalent of {binary_number} is: {decimal_result}\n")
        elif choice == '3':
            print("Exiting the converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
