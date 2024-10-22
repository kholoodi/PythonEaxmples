#an empty set 
s = {}
print(s)
myset = {1, -2, 2, 0, (1,2,3), frozenset({1,2,3}),'Hello', True }
print(myset)

#set() function uses for create a set or transform the data type to set
x = set(frozenset({ 1, 2, 3, 4}))
y = set((1, 2, 3))
z = set([1,2,3])
e = set(set ())
f = set()
print(type(x))
print(type(y))
print(type(z))
print(type(e))
print(type(f))