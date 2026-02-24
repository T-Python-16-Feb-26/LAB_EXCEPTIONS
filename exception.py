def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x+b)
        #print("Addition:", x+'hi')
    
    except NameError:
        print("NameError: variable 'b' is not defined")

    #except Exception:
        #print("some error happend")
        
    
    else:
        print("The operation is successful")

additoin(10, 20)
