#Python string-dncoding with dncode() function
str0 = "Welcom toُ Python"
enstr0 = str0.encode(encoding='utf8')
print('The encoding string is : ')
print(enstr0)
print('The decodein string is: ')
print(enstr0.decode('UTF-8', 'strict'))