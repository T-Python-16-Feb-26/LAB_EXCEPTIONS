
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5)+32

def main():
    while True:
        try:
            user_input = input('Enter a temprature and its unit (e.g. , "25 C" or "77 F") : ')
            temp, unit= user_input.split()
            temp = float(temp)
            unit = unit.upper()
            if unit == "C":
                result = celsius_to_fahrenheit(temp)
                print(f"Temperature in Fahrenheit: {result:2f} F" )
                break
            elif unit == "F":
                result = fahrenheit_to_celsius(temp)
                print(f"Temperature in Celsius: {result:2f} C" )
                break
            else:
                raise TypeError
            
        except ValueError:
            print ("Invalid temeprature value. please try again.")
        except TypeError:
            print("Invalid unit. please use 'C' for celsius or 'F' for fahrenheit ")
main()