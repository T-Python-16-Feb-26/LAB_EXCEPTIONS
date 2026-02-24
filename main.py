def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)

except NameError:
    print("Variable is not defined")
except Exception as e:
    print(e.__class__)
else:
    print("the operation is successful")
