

def additoin(x, y):
    x = 10
    y = 20
    try:
        print("Addition:", x + b) #nameError. variable 'b' is not defiend 
        print("the operation is successful")
    except NameError:
        print("Error: A variable is not defined.")

additoin(10, 20)
