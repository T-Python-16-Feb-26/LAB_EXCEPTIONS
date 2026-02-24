
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

def main():
 while True:
  try:
    user_temp=input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
    number,unit=user_temp.split()
    temp_value=float(number)
    if unit.upper() =="C":
     result=celsius_to_fahrenheit(temp_value)
     print(f"{result:.2f} F")
     break
    elif unit.upper() =="F":
     result=fahrenheit_to_celsius(temp_value)
     print(f"{result:.2f} C")
     break
    else:
      raise TypeError
  except ValueError:
    print("Error: Wrong temperature")
  except TypeError :
    print("Use C or F only")

main()







