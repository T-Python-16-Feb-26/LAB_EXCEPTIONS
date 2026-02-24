"""
# Bonus
##  Temperature Converter

Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter that accepts 
user input and converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.

"""
"""
    1. Write a function `celsius_to_fahrenheit(celsius)` that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit.
    Use the formula `fahrenheit = (celsius * 9/5) + 32`.
 """
def celsius_to_fahrenheit(celsius:float) -> float:
    """This function takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit."""
    return (celsius * 9/5) + 32

"""
    2. Write a function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. 
    Use the formula `celsius = (fahrenheit - 32) * 5/9`.
"""
def fahrenheit_to_celsius(fahrenheit:float) -> float:
    """This function takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius."""
    return (fahrenheit - 32) * 5/9

"""
    3. Write a `main` function that:
        - a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), 
        separated by a space (e.g., "25 C" or "77 F").
        - b. Splits the input string into a temperature value and its unit.
        - c. Tries to convert the input temperature to its opposite unit using the appropriate function 
        (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
        - d. Riases & handles the following exceptions:
            - `ValueError`: If the user enters an invalid temperature value, display an error message and prompt the user to try again.
            - `TypeError`: raise this error  If the user enters an invalid unit, display an error message and prompt the user to try again.
        - e. If the conversion is successful, print the converted temperature and its unit.
"""
def main():
    msg = "Enter a temperature and its unit (either \"C\" for Celsius or \"F\" for Fahrenheit), separated by a space (e.g., \"25 C\" or \"77 F\")."
    print("-"* len(msg))
    print(msg)
    print("or (q) to exit.")
    print("-"* len(msg))
    while True:
        try:
            user_input = input("- ")
            if user_input.lower() == "q":
                break
            value, unit = user_input.split()
            unit = unit.upper()
            value = float(value)

            if unit == "C":
                print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(value):.2f} F")
            elif unit == "F":
                print(f"Temperature in Celsius: {fahrenheit_to_celsius(value):.2f} C")
            else:
                raise TypeError("Invalid Unit")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Brother... Stop playing around, you are either not giving us a unit or giving us extra units")
            print("it must be, value followed by space then unit. (e.g., (25 C) or (77 F)")
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__} – {e}")
    for i in range(10):
        print(" |")
    print("Cya")


"""
    4. Call the `main` function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.
"""
if __name__ == "__main__":
    main()

"""

Example Output:

```
Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100 F
Temperature in Celsius: 37.78 C

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 50 C
Temperature in Fahrenheit: 122.0 F

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 25 X
Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100.5 F
Temperature in Celsius: 38.06 C
```
"""