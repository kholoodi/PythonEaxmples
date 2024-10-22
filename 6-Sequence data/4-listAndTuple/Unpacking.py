''' When we create list or tuple we do "Packing" 
The "Unpacking" is tran the the list or tuple items to individual variables.
lets see the examples:
'''
# Unpacking List 
fruits = ["Bananas", "Apples",   "Grapes"]
[red, yellow, green] = fruits
print(yellow)
print(red)
print(green)

print("****************")
# Unpacking Tuple 
fruits = ("Bananas", "Apples",   "Grapes")
(red, yellow, green) = fruits
print(yellow)
print(red)
print(green)
#OR
fruits = ("Bananas", "Apples",  "Grapes", "Kiwis")
(red, yellow, *green) = fruits
print(yellow)
print(red)
print(green)
#OR
fruits = ("Bananas",  "Grapes", "Kiwis","Apples" )
(yellow, *green, red) = fruits
print(yellow)
print(green)
print(red)