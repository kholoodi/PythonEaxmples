# There are some functions for removing elements from the list .

list = [1,2, 3, "Hi", "hello", [5,6,"OK"], 8]
print(list)
#remove() function for remove particular element by its value.
list.remove(3)
print(list)
#pop() function for remove the last element of the list.
list.pop(4)
print(list)
list.pop()
print(list)

#clear() function for remove all elements from the list. 
list.clear()
print(list)

#del() function for remove the entire list.
del(list)
print(list)