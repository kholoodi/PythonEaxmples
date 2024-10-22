
d1 = {'id': 1, 'name': 'Noor', 'size': 37, 'age':26}

#The pop() function used to remove particular dictionary item  via item's key.
d1.pop('id')
print(d1)
#The popitem() function removes the last items in the dictionary.
d1.popitem()
print(d1)

#clear() function removes all the items in the dictionary.
d1.clear()
print(d1)

#del() function used to remove the entire dictionary .
del d1['size']
print(d1)
