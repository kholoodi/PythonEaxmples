#The list contains different types of data like numbers or strings or even lists or tuples
list = [1,2, 3, "Hi", "hello", [5,6,"OK"], (1,2,3),8 ] 
#Access to elements
print(list[7]) 
print(list[-1])

list = [1,2, 3, "Hi", "hello", [5,6,"OK"], 8]
print(list[:3])
print(list[3:5])

#List changing
list = [1,2, 3, "Hi", "hello", [5,6,"OK"], 8]
list[1] = 4
print(list)