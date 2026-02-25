def additoin(x, y):
    x = 10
    y = 20
    
    # this line will raise a NameError
    # because variable 'b' is not defined
    print("Addition:", x + b)


# try to execute the function
try:
    additoin(1, 2)

# handle the specific exception (NameError)
except NameError as ne:
    print("Error:", ne.__class__.__name__)  
    print("A variable is not defined inside the function.")

# handle any other unexpected exception
except Exception as e:
    print("Unexpected error:", e.__class__.__name__)

# if no exception occurs
else:
    print("the operation is successful")