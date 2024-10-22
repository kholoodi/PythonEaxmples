#String variables can be declared either by using single or double quotes:
str= 'Hello,World'
#same as
str= "Hello,World"



#Multiple line text
x = """ Hello,world 
    Hello,world 
    Hello,world 
    """
#OR
x = ''' Hello,world 
    Hello,world 
    Hello,world 
    '''
#String Concatenation
a , b = 'Hello','World'
print(a +" "+ b)

#str() function
x = str(1)
y = str(1.5)
z = str(True)
print(type(x))
print(type(y))
print((type(z)))

#format() function 
size = 37
price = 88.50
text = " The shoes  size is {0}, and its price is {1}"
print(text.format(size,price))
# spaces formatting
print(" The shoes  size is {0:<5}, and its price is {1:>5}".format( size,price))
# for  + formatting
print(" The shoes  size is {0:<5}, and its price is {1:+}".format( size,price))
print(" The shoes  size is {0:<5}, and its price is {1:+05}".format( size,price))
#can use any name
print(" The shoes  size is {x}, and its price is {y}".format(x = price,y= size))
print(" The shoes  size is {x}, and its price is {y}".format(x = size,y= price))

#string function
s = 'Welcome to Python programming'
print(s.upper())
print(s.lower())
print(s.casefold())
print(s.capitalize())
print(s.swapcase())

