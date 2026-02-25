def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    while True:
        user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        
        try:
            value, unit = user_input.split()
            temperature = float(value)

            if unit.upper() == "C":
                result = celsius_to_fahrenheit(temperature)
                print("Temperature in Fahrenheit:", round(result, 2), "F")
                break

            elif unit.upper() == "F":
                result = fahrenheit_to_celsius(temperature)
                print("Temperature in Celsius:", round(result, 2), "C")
                break

            else:
                raise TypeError

        except ValueError:
            print("Invalid temperature value. Please enter a numeric value.")

        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")


main()