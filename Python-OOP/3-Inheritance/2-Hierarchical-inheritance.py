# Hierarchical inheritance
# Base class 
class A:
	def func1(self):
		print("This is A class.")

# Derived class 1
class B(A):
	def func2(self):
		print("This is B class.")
		
# Derived class 2
class C(A):
	def func3(self):
		print("This is C class.")

def main():
 obj0 = B()
 obj0.func1()
 obj1 = C()
 obj1.func1()
 
if __name__ == '__main__':
  main()
