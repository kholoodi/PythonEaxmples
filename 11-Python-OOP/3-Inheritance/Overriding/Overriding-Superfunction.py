#Overriding super function
# Base class
class A:
	def func(self):
		print("This is A class.")

# Derived class
class B(A):
	def func(self):
	  #Overriding for "func()" method in a base class using super function
	  super().func()
	  print("This is B class.")
		
def main():
  obj0 = B()
  obj0.func()

if __name__ == '__main__':
  main()
