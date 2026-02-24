
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius



def main():
    while True:
        try:
            
            user_input = input("Enter temperature and unit (e.g., 29 C or 87 F): ")

            
            parts = user_input.split()

            
            value = float(parts[0])

            
            unit = parts[1].upper()

            
            if unit == 'C':
                result = celsius_to_fahrenheit(value)
                print("Temperature in Fahrenheit:", round(result, 2), "F")
                break

            elif unit == 'F':
                result = fahrenheit_to_celsius(value)
                print("Temperature in Celsius:", round(result, 2), "C")
                break

            else:
                
                raise TypeError

        
        except ValueError:
            print("Invalid temperature. Please enter a number.")

        
        except TypeError:
            print("Invalid unit. Please use 'C' or 'F'.")

        
        except Exception:
            print("Invalid input. Try again.")



main()
