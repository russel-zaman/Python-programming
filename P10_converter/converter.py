def temp_converter(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "F" and to_unit == "K":
        return (value + 459.67) * 5/9
    elif from_unit == "K" and to_unit == "F":
        return (value * 9/5) - 459.67
    else:
        return value

def currency_converter(value, from_unit, to_unit):
    # Add your currency conversion rates here
    rates = {"USD": 1, "EUR": 0.85, "GBP": 0.73, "JPY": 109.34}
    if from_unit in rates and to_unit in rates:
        return value * rates[to_unit] / rates[from_unit]
    else:
        return value

def volume_converter(value, from_unit, to_unit):
    # Add your volume conversion factors here
    factors = {"m3": 1, "L": 1000, "gal": 0.264172}
    if from_unit in factors and to_unit in factors:
        return value * factors[to_unit] / factors[from_unit]
    else:
        return value

def mass_converter(value, from_unit, to_unit):
    # Add your mass conversion factors here
    factors = {"kg": 1, "g": 1000, "lb": 2.20462}
    if from_unit in factors and to_unit in factors:
        return value * factors[to_unit] / factors[from_unit]
    else:
        return value

def main():
    unit_types = {
        "temperature": ["C", "F", "K"],
        "currency": ["USD", "EUR", "GBP", "JPY"],
        "volume": ["m3", "L", "gal"],
        "mass": ["kg", "g", "lb"]
    }

    print("Unit Converter")

    from_type = input("Enter the type of unit being entered (temperature, currency, volume, mass): ").lower()
    if from_type not in unit_types:
        print("Invalid unit type")
        return

    to_type = input("Enter the type of unit you want to convert to (temperature, currency, volume, mass): ").lower()
    if to_type not in unit_types:
        print("Invalid unit type")
        return

    from_unit = input(f"Enter the {from_type} unit being entered ({', '.join(unit_types[from_type])}): ").upper()
    to_unit = input(f"Enter the {to_type} unit you want to convert to ({', '.join(unit_types[to_type])}): ").upper()

    value = float(input(f"Enter the value in {from_unit}: "))

    if from_type == to_type:
        converted_value = value
    elif from_type == "temperature":
        converted_value = temp_converter(value, from_unit, to_unit)
    elif from_type == "currency":
        converted_value = currency_converter(value, from_unit, to_unit)
    elif from_type == "volume":
        converted_value = volume_converter(value, from_unit, to_unit)
    elif from_type == "mass":
        converted_value = mass_converter(value, from_unit, to_unit)

    print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")

if __name__ == "__main__":
    main()
