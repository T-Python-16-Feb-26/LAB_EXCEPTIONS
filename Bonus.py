def celsius_to_fahrenheit(temp,unit):
    fahrenheit = (temp * 9/5) + 32
    unit = "F"

    return fahrenheit,unit

def fahrenheit_to_celsius(temp,unit):
    celsius = (temp - 32) * 5/9
    unit = "C"
    return celsius,unit


def main():
    while True:
        try: 
            user_input = input("Enter temperature and unit (e.g., 25 C or 77 F): ")

            temp, unit = user_input.split()
            temp = float(temp)
            if unit != "C" and unit != "F":
                raise TypeError("Enter a valid unit")
            
            if unit == "C":
                result = celsius_to_fahrenheit(temp,unit)
            elif unit == "F":
                result = fahrenheit_to_celsius(temp,unit)
        except ValueError:
            print("Invalid temperature value")
        except Exception as e:
            print(e)
        else:
            print(f"{round(result[0],2)} {result[1]}")
            break

main()
