#string work withe (+) and (*) operators
str1 = 'Welcome to '
str2 = 'Python'
print( str1 + str2)
print ( str2 * 3)

#String is sequence data, so it uses indexes
str1 = 'Welcome to Python'
print (str1[1])
print(str1[11:17])
print(str1[11:])
print(str1[:-9])

# Can use the (%) Coordinator with string 
#print one letter 
print(" Welcome to %cython"%('P'))
#(%s)print string 
#(%d)print number with decimal format or (%i) print an integer numbe
print(" Welcome to %s %i"%('Python', 3))
print(" Welcome to %s %d"%('Python', 3))
a = 12
#print number with octal format
print(" 12 in Octal is  =  %o"%(a))
#print number with hexadecimal format 
print(" 12 in hexadecimal  is  =  %x or %X"%(a, a))
#print number with float format 
print(" %f"%(a))

#using Escape Characters withe string 
str1 = 'Welcome \t to \n \"Python\"'
print(str1)

#using Raw String- (R/r) with string 
print( r'\\ Welcome to Python')
print( R"\\ Welcome to Python")
