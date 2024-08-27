#Overriding - Class name 
# Base class 
class A:
	def __str__(self):
		return"This is A class."

# Intermedirctory class
class B(A):
	def __str__(self):
		return"This is B class."
		
# Derived class
class C (B):
	def __str__(self):
	  
	  return A.__str__(self) + '\nThis is C class.'


def main():
  obj0 = C()
  print(obj0)
  
if __name__ == '__main__':
  main()
  