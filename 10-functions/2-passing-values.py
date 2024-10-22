#Example 1
#function recive the parameters 
def printwelcom(str):
    print(str)

printwelcom("Welcom to Python")
###########################################
#Example 2
 #function can receive the parameters and return a value
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#Calling 
print(power(2))
print(power(3))
print(power(2, 3))
print(power(3, 2))
###########################################
#Example 3
 #function can receive unknow parameters numbers  and return a value
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#Calling 
print(multi_add(1))
print(multi_add(1, 2))
print(multi_add(1, 2, 3))
print(multi_add(1, 2, 3, 4))
###########################################

