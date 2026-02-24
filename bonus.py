def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    while True:
        try:
            input_temp = input("Enter a temperature with its unit (e.g., 25 C or 77 F): ")
            splitted_input = input_temp.split()

            if len(splitted_input) != 2:
                raise ValueError("Invalid input format.")
            
            temp_value, unit = splitted_input

            temperature = float(temp_value)
            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {result:.1f} F")
                break
            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {result:.2f} C")
                break

            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            
        except ValueError as ve:
            print("Invalid temperature value. Please enter a numeric value.")

        except TypeError as te:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

main()
            




