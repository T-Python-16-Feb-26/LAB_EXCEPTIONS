def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    while True:
        try:
            user_input = input(
                'Enter a temperature and its unit (e.g., "25 C" or "77 F"): '
            )

            value, unit = user_input.split()

            value = float(value)
            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(value)
                print(f"Temperature in Fahrenheit: {result:.2f} F")
                break

            elif unit == "F":
                result = fahrenheit_to_celsius(value)
                print(f"Temperature in Celsius: {result:.2f} C")
                break

            else:
                raise TypeError("Invalid unit. Please use 'C' or 'F'.")

        except ValueError:
            print("Invalid temperature value. Please try again.")

        except TypeError as e:
            print(e)


main()