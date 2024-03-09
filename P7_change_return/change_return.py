def calculate_change(cost, amount_given):
    # Calculate the change
    change = amount_given - cost

    # Convert change to cents
    change_in_cents = int(change * 100)

    # Calculate the number of quarters, dimes, nickels, and pennies
    quarters = change_in_cents // 25
    dimes = (change_in_cents % 25) // 10
    nickels = ((change_in_cents % 25) % 10) // 5
    pennies = ((change_in_cents % 25) % 10) % 5

    return change, quarters, dimes, nickels, pennies

def main():
    # Input from the user
    cost = float(input("Enter the cost of the item: $"))
    amount_given = float(input("Enter the amount of money given: $"))

    # Calculate change details
    change, quarters, dimes, nickels, pennies = calculate_change(cost, amount_given)

    # Output the results
    print(f"\nChange: ${change:.2f}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

if __name__ == "__main__":
    main()
