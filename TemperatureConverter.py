def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    while True:
        try:
            Temperature , unit = input('Enter temperature and unit (e.g. "25 C"): ').split()

            Temperature  = float(Temperature ) 

            if unit.upper() == "C":
                print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(Temperature ):.2f} F")
                break

            elif unit.upper() == "F":
                print(f"Temperature in Celsius: {fahrenheit_to_celsius(Temperature ):.2f} C")
                break

            else:
                raise TypeError 

        except ValueError:
            print("Invalid temperature value. Try again.")

        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit")


main()