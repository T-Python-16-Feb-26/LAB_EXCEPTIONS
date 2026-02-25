def addition(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)  # b is not defined

        print("The operation is successful")

    except NameError:
        print("Error: A variable is not defined (NameError occurred)")
        print("Operation failed")


addition(10, 20)