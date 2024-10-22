# Dictionary items access
d1 = {'id': 1, 'name': 'Noor', 'size': 37}

#The values() function for access to dictionary values only.
print(d1.values())
#The keys() function for access to dictionary keys only.
print(d1.keys())

#The items() function for access to values and keys together. 
print(d1.items())

#To access for particular item in the dictionary.
print(d1['name'])
#Using get() function to access for particular item in the dictionary via its key.
print(d1.get('name'))

#Also can use if...in to check if the item is in the dictionary 
if 'name' in d1:
    print("Yes, the name is " + d1['name'])