x, y = 100, 10
if x < y:
	print('x < y: x is {} and y is {}'.format(x, y))
else:
	print('x >= y: x is {} and y is {}'.format(x, y))
print('The end')


#short format
print('x < y') if x < y else print('x >= y')