tuple1 = () # an empty tuple 
# tuples as lists can contain different types of data like numbers or strings or even lists or tuples
tuple12 = (1,2, 3, "Hi", "hello", [5,6,"OK"], (1,2,3), 8)

#The comma is important to declare tuple
tuple0 = (1) # integer type
print(type(tuple0))
tuple1 = (1,)  # tuple type
print(type(tuple1))

#Any gruple of data is tuple by  default. 
x = 'Hi', 'Welcome', 1, 2, 3, True
print(type(x)) # x  is belong to the <class 'tuple'>

#Access to the tuple items. 
tuple = (1,2, 3, "Hi", "hello", [5,6,"OK"], 8)
print(tuple[6])
print(tuple[-1])
print(tuple[:3])
print(tuple[3:5])
