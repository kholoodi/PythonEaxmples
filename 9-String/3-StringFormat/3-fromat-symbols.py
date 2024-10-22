#Python string-format (symbols / spaces )
x = -15
y = 17
print('the numbers are :{0:} {1:5}'.format(x , y)) 
print('the numbers are :{0:<5} {1:>5}'.format(x , y)) 
print('the numbers are :{0:^5} {1:^5}'.format(x , y)) 
print('the numbers are :{0:=5} {1:+}'.format(x , y))   
print('the numbers are :{0:-} {1:}'.format(x , y))   
print('the numbers are :{0:<5} {1:+5}'.format(x , y))   
print("===================================")
z = 15 * 354 * 1000 
print('the number  is :{:_} '.format(z)) 
print('the number  is :{:,} '.format(z))   
print('the number  is :{:,} '.format(z).replace(',','.')) 
print('the number  is :{:f} '.format(z)) 
print('the number  is :{:.3f} '.format(z)) 

#The short formal formating
x = 45
print(f'the number is :{x:.3f} ')