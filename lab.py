"""
# LAB_EXCEPTIONS


## Below you have a code that raises an exception , using what you learned do the following:
- Find what type of exception is raised.
- Hanlde the exception in try..except 
- If operation successful , print "the operation is successful"
- if operation fails, handle the specific exception that is raised , and print a relevant message.
```
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)
```
"""
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

print("--Finding out what exception is raised")
try:
    additoin(10, 20)
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} – {e}")

print()
print("--Handeling exception")
try:
    additoin(10, 20)
except NameError:
    print("Name error -- Undefined name")
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} – {e}")  
else:
    print("the operation is successful")