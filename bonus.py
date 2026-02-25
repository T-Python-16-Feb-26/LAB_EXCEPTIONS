def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        try:
            user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
            temp_str, unit = user_input.split()

            temperature = float(temp_str)

            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenhite: {result:.2f} F")
                break
            
            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {result:.2f} C")
                break

            else:
                raise TypeError
            
        except ValueError:
            print("invalid temperature value, please enter a valid number.")

        except TypeError:
            print("invalid unit, please use 'C' for Celsius or 'F' for Fahrenheit.")


main()
