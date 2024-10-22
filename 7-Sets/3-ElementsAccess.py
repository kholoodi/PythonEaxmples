#we can access to the set's element vis loop
myset = {1, -2, 2, 0, (1,2,3), frozenset({1,2,3}),'Hello', True }
for x in myset:
    print(x)
    
#Check if 'Hi' is an item in myset
print( 'Hi' in myset)