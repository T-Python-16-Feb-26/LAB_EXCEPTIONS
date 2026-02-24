'''

'''
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
    print("operation successful")
except NameError as B:
    print("please make sure the input value is defined and correct \n more context: ", B)
except Exception as e:
    print(e)