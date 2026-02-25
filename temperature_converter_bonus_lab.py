# Converts a temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Converts a temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Parses a temperature input string and separates it into numeric value and unit
def parse_input(user_input):
    user_input = user_input.replace(" ", "")
    
    value = float(user_input[:-1])     
    unit = user_input[-1].upper()
    
    if unit not in ("C", "F"):
        raise TypeError("Invalid unit")
    
    return value, unit

# Main function to run the temperature converter
def main():
    temp = input('Enter a temperature and its unit (e.g., "25 C" or "77F"): ')
    
    value, unit = parse_input(temp)
    
    if unit == "C":
        result = celsius_to_fahrenheit(value)
        print(f"Temperature in Fahrenheit: {round(result, 2)} F")
    else:
        result = fahrenheit_to_celsius(value)
        print(f"Temperature in Celsius: {round(result, 2)} C")


# Infinite loop to repeatedly ask the user for input until valid
while True:
    try:
        main()
        break
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
    except TypeError:
        print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    except Exception as e:  # Catch any unexpected exceptions and print their class for debugging
        print(e.__class__)