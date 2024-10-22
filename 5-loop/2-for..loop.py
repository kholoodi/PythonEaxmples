# use a for loop over a collection
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:
    print (d)


#using the enumerate() function to get index 
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i, d in enumerate(days):
    print (i, d)

#using range() function with for loop
for i in range(3):
    print(i)
print('-----------')
for x in range(5,10):
	print(x)
     
#Using else with for
for x in range(5,10):
    print(x)
else:
    print('x is not in the range from 5 to 10')