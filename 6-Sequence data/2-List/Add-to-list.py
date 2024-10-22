# There are some functions for adding elements to the list .
list1 = [3, 4, 5]
list2 = [8, 7, 9]

#append() function for add elements at the end list.
list1.append(8)
print(list1)

#insert() function for add elements at the particular position in the list.
list1.insert(2, 9)
print(list1)

#extand() function for merge two lists.
list1.extend(list2)
print(list1)