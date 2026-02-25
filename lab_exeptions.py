def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)   # b غير معرف


try:
    additoin(10, 20)
    print("the operation is successful")

except NameError:
    print("Error: variable 'b' is not defined")

except Exception:
    print("Operation failed")