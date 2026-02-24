def additoin(x, y):
    try:
        x = 10
        y = 20

        # raise NameError (b is not defined so)
        print("Addition:", x + b)

    except NameError:
        print("Error: Undefined variable used in the operation.")

    else:
        print("the operation is successful")


additoin(10, 20)