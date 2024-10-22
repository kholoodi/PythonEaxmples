#Two function used for intersection  sets intersection() and intersection_update() function, see the example:
A = { 1, 2, 3, 4}
B = { 3, 4, 5, 6 }
# using intersection()
x = A.intersection(B)
print(x)
# using intersection_update()
A.intersection_update(B)
print(A)