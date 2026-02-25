def additoin(x, y):
   try:
    x = 10
    y = 20
    print("Addition:", x + y)
   except NameError as Ne:
     print(Ne)
   except Exception as e:
     print(e.__class__)
   else:
     print("the operation is successful")


additoin(10, 20)