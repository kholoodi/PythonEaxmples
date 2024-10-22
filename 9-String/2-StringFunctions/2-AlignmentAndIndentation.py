#Functions that adjust alignment and indentation

#expandtabs() function for control the space of "\t" between letters
str1 = "P\ty\tt\th\to\tn"
print(str1.expandtabs())
print(str1.expandtabs(3))
print(str1.expandtabs(6))
print(str1.expandtabs(12))

#ljust() and  rjust() functions
str1 = "Welcome to Python"
print(str1.ljust(30) , " 3")
print(str1.ljust(30, "*") , " 3")
print(str1.rjust(30) , " 3")
print(str1.rjust(30, "*") , " 3")

#center() function
print(str1.center(30))
print(str1.center(30, '*'))

#strip(), lstrip()  and rstrip() functions 
str1 = "    Welcome to Python    "
str2 = "eee...Welcome to Python,,,ccc"
print(str1.strip())
print(str2.strip("e.,c"))
print(str1.lstrip())
print(str2.lstrip("e."))
print(str1.rstrip())
print(str2.rstrip(",c"))

