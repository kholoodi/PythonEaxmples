d1 = {'id': 1, 'name': 'Noor', 'size': 37, 'age':26}
#Return the dictionary keys by using for loop
for i in d1:
    print(i)
#OR
for i in d1.keys():
    print(i)

#Return the dictionary values by using for loop
for i in d1:
    print(d1[i])
#OR
for i in d1.values():
    print(i)

#Return the dictionary items by using for loop
for x ,y in d1.items():
    print(x , y)