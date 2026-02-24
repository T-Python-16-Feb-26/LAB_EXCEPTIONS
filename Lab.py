def addition(x,y):
        x=10
        y=20
        print("Addition: ",x+b)
   
try:
    addition(10,20)
except NameError as e:
    print("Error type: ",e.__class__)
    print("Message: ",e)
except Exception as e:
    print("Error type: ",e.__class__)
    print("Message: ",e)
else:
    print("the operation is successful")