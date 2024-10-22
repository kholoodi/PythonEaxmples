myset = {1, -2, 2, 0, (1,2,3), frozenset({1,2,3}),'Hello', True }
#remove() and discard() functions used to remove particular element via element's value.
myset.remove(2)
print(myset)
myset.discard('Hello')
print(myset)
#pop() function removes the last element in the set.
myset.pop()
print(myset)
#clear() function removes all the elements in the set.
myset.clear()
print(myset)
#del() function used to remove the entire set.
del(myset)