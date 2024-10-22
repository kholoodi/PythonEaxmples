'''Tuples are immutable, which means we cannot change, 
add or remove elements after the tuple is created. 
To be able to update a tuple we use two ways:
1- using + and * operators. 
2-convert tuple to list and work with list functions for adding or removing items 
'''
t = (1,2, 3, "Hi", "hello", [5,6,"OK"], 8)
y = list(t) # list() function to convert to list
y.pop()
y.insert(1,5)
t = tuple(y) # tuple() function to convert yo tuple
print(t)