#Python join and split string functions 
tuple1 = ("Welcome", "To", "Python")
list1 = ["Welcome", "To", "Python"]
dir1 = {"name":"Mona", "country": "Saudi Arabia"}
str1 = "Python"
str2 = "123"
print("*".join(tuple1))
print(",".join(list1))
print("-".join(dir1))
print("+".join(str2))
print(str2.join(list1))
print(str1.join(str2))
print(str2.join(dir1))