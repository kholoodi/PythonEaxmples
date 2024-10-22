#Two function used for intersection  sets symmetric_difference() and symmetric_difference_update() function, see the example:
A = { 1, 2, 3, 4}
B = { 3, 4, 5, 6 }
#Using symmetric_difference() function
x = A.symmetric_difference(B)
print(x) 
#Using symmetric_difference_update() function
A.symmetric_difference_update(B)
print(A)