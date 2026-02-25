def celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        user_input = input("enter a temperature and its unit (either C for Celsius or F for Fahrenheit): ")
        if " " not in user_input:
            user_input = user_input[:-1] + " " + user_input[-1]
        try:

            value, unit =user_input.split()
            value = float(value)

            if unit.upper() == "C":
                in_f = celsius_to_fahrenheit(value)
                print(f"temperature in fahrenheit: {in_f} F")
                break
        
            elif unit.upper() == "F":
                in_c = fahrenheit_to_celsius(value)
                print(f"temperature in Celsius: {in_c} C")
                break

            else:
                raise TypeError
        
        except ValueError:
            print("invalid value, please enter a number")
        except TypeError:
            print("invalid unit, please use C or F")
            


        

main()