def addition(x,y):
    x=10
    y=20
    print("addition:",x+y)

try:
        addition(10,20)
except NameError as e:
        print(f"Error : a variable is not defined ({e})")
except Exception as e:
        print(f"an unexcepted error occurred:{e}")
else:
        print("the operation is successful")

    