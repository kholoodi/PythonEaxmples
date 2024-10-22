# Each varable has id number, this id is variable location in memory 
x = 1
# Using id() function to show variable id 
print(id(x))
#The different values to same variables name takes different id
x = 2
print(id(x))
x = 'Hi'
print(id(x))