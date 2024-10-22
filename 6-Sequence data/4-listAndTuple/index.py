#Index() function returns the index of list or tuple items
#index() with list 
list = [1, 2, 3, "Hi", "hello", [5,6,"OK"], (1,2,3), 8 ]
x = list.index([5,6,"OK"])  
print(x)

print("--------------------")
#index() with tuple 
tuple1 = (1,2, 3, "Hi", "hello", [5,6,"OK"], (1,2,3), 8)
print(tuple1.index("Hi"))