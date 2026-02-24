def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True: 
        user_input = input("Enter the temperature and unit (C or F): ")
        
        try:
            temp_str, unit = user_input.split()  
            temp = float(temp_str)  
            unit = unit.upper()
            
            if unit == "C":
                converted = celsius_to_fahrenheit(temp)
                print(f"Temperature in Fahrenheit: {converted:.2f} F")
                break  
            elif unit == "F":
                converted = fahrenheit_to_celsius(temp)
                print(f"Temperature in Celsius: {converted:.2f} C")
                break
            else:
                raise TypeError  
            
        except ValueError:
            print("Wrong input Please enter a number followed by C or F")
        except TypeError:
            print("Invalid unit Please use 'C' for Celsius or 'F' for Fahrenheit.")

main()