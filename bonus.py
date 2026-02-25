def celsius_to_fahrenheit(celsius: float):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            temperature, unit = user_input.split()
            try:
                float_temperature = float(temperature)
            except ValueError:
                raise ValueError("Invalid temperature value. Please enter a numeric value.")
            
            unit = unit.upper()
            if unit != "C" and unit != "F":
                raise TypeError("Invalid unit. Please use 'C' or 'F' only.")
            
            if unit == "C":
              print(f"Temperature in Fahrenheit {round(celsius_to_fahrenheit(float_temperature), 2)} F")
              break
            elif unit == "F":
              print(f"Temperature in Celsius {round(fahrenheit_to_celsius(float_temperature), 2)} C")
              break
 

        except Exception as e:
         print(e)

        else:
          print("The operation is successful")


main()