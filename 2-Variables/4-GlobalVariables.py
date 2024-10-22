# Declare variables and initialize it
x = "abc"
y = 'ABC'
print (x)
print(y)

# Global vs. local variables in functions
def someFunction():
    global x  # but x as global variable
    x = 'x'
    y = 'y'
    print (x)
    print(y)

someFunction()
print(x)
print(y)