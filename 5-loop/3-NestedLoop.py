# nested  while loop
x = 0
while x < 5:
    y = 0
    print('****')
    while y <= x :
      y += 1
      print(y)
    x += 1

#Nested for loop
for i in range(5):
    print('****')
    for x in range(3):
      print(x)


 #Nested for and while loops 
for i in range(5):
    x = 0
    while x < i:
      print(x)
      x += 1
    print('****')