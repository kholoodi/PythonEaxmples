#Two function used for intersection  sets difference() and difference_update() function, see the example:
A = { 1, 2, 3, 4}
B = { 3, 4, 5, 6 }
#Using difference() function
x = A.difference(B)
print(x)
#Using difference_update() function
A.difference_update(B)
print(A)