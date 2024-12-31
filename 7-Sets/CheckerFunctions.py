A = { 1, 2, 3, 4}
B = { 3, 4, 5, 6 }
C = {7, 8, 9}
D = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#The isdisjoint() function checks for intersection between two sets and returns false if there is no intersection.
print(A.isdisjoint(B)) 
print(A.isdisjoint(C)) 

#The issubset() function checks if the first set is subset from the second set. 
print(C.issubset(D))
print(D.issubset(C))

#The issuperset() function that checks if the first set is a superset of the second set.
print(D.issuperset(C))
print(C.issuperset(D))