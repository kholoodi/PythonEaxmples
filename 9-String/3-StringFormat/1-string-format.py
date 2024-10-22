#Python format() function used
x = 15 
y = 10
print('the numbers are :{} {}'.format(x , y))
print('the numbers are :{0} {1}'.format(x , y))
print('the numbers are :{1} {0}'.format(x , y))
print("===================================")
print('the numbers are :{a} {b}'.format(a =x , b = y))
print('the numbers are :{b} {a}'.format(b =x , a = y))
print("===================================")
str1 = "The grade is {grade: .2f}"
print (str1.format(grade = 77.753))