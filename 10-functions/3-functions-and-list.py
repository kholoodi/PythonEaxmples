#Example 1
#In python functions  we can use list as arrgumrnt 
def changList( list1 ):
   list1 = [10, 20,30, 40] 
   print ("The list value/'s inside changList function: ", list1)
   return

#The List outside the function
mylist = [1,2,3] 
changList( mylist )
print ("The list value/'s outside changList function: ", mylist)
###########################################
#Example 2
#With function can do change in list values 
def changElement( List1 ):
   print ("The list value/'s inside changElement function before change: ", List1)
   List1[2]=0
   print ("The list value/'s inside changElement function after change: ", List1)
   
mylist = [1,2,3] 
changElement( mylist )
print ("The list value/'s outside and after the changElement function: ", mylist)
###########################################
#Example 3
#With function can do change in list values 
def changeList(List2):
   print ("The list value/'s inside changeList function before change: ", List2)
   for i in range (len(List2)):
      List2[i] = 0
   print ("The list value/'s inside changeList function after change: ", List2)

mylist = [1,2,3] 
changeList(mylist)
print ("The list value/'s outside and after the changeList function: ", mylist)