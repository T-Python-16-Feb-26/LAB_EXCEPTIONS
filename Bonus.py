def celsius_to_fahrenheit(celsius):
    return round((celsius*9/5)+32,2)
    
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit-32)*5/9,2)
    
def main_function():
    while True:
        user_input = input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
        
        try:
            value , unit = user_input.split()
            value = float(value)
            unit =unit.upper()
            if unit == "C":
                result = celsius_to_fahrenheit(value)
                print(f"Temperature in Fahrenheit: {result}°F")
                break
            elif unit == "F":
                result = fahrenheit_to_celsius(value)
                print(f"Temperature in Celsius: {result}°C")
                break
            else:
                raise TypeError
            
        except ValueError :
            print("The input value is incorrect")

        except TypeError :
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        
main_function()


    

