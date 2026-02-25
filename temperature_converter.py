def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    while True:
        try:
            user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')

            # تقسيم الإدخال
            temp, unit = user_input.split()

            # تحويل الرقم
            temp = float(temp)

            # جعل الحرف كبير
            unit = unit.upper()

            # التحويل
            if unit == "C":
                result = celsius_to_fahrenheit(temp)
                print(f"Temperature in Fahrenheit: {result:.2f} F")
                break

            elif unit == "F":
                result = fahrenheit_to_celsius(temp)
                print(f"Temperature in Celsius: {result:.2f} C")
                break

            else:
                raise TypeError

        except ValueError:
            print("Invalid temperature value. Please enter a number.")

        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")


main()