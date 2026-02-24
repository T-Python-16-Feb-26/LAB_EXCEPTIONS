def addition(x,y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    addition(10,20)
except NameError as e:
    print("NameError occurred: A variable is used that has not been defined")
else:
    print("the operation is successful")
