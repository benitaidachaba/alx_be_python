# 🌍 Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Try converting to float

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")

        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")

        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Error: {e if str(e) else 'Invalid temperature. Please enter a numeric value.'}")

if __name__ == "__main__":
    main()
# This code provides a temperature conversion tool that allows users to convert between Celsius and Fahrenheit.
# It uses global conversion factors for the calculations and handles user input with error checking.