def celsuis_to_fahrenheit(celsius):
    return (celsius *9/5)+32
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit -32)*5/9
def main():
    while True:
        try:
            user_input=input('enter a temperature and it is unit C of F')
            parts=user_input.split()
            if len(parts) !=2:
                raise ValueError("invaild format plz provid both value and unit")
            value=float(parts[0])
            unit=parts[1].upper()
            if unit=="C":
                result = celsuis_to_fahrenheit(value)
                print(f"temperature in fahrenheit:{round(result,2)}F")
                break
            elif unit=="F":
                result=fahrenheit_to_celsius(value)
                print(f"temperature in celsius :{round(result,2)}C")
                break
            else:
                raise TypeError("invaild unit ,plz use 'C' for celsius or 'F' for fahernhiet")
            
        except ValueError:
            print("invaild temp value ,plz enter a vaild number")
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"something went wrong:{e}")
main()
            
            