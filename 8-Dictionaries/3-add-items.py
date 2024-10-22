# The update() function uses to do change dictionary or add items to the dictionary. 
d1 = {'id': 1, 'name': 'Noor', 'size': 37}
print(d1)
#Here update() function change the "id"  value 
d1.update({'id': 2})
print(d1)
# Now update() function add the new item to "d1" 
d1.update({'Age': 26})
print(d1)

#The setdefault() function returns the item's value with the specified key. 
# If the key does not exist, it adds the key with the specified value.
print(d1.setdefault('size'))
x = d1.setdefault('age', 26)
print(d1)