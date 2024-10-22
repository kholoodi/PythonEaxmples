# Hybrid inheritance
# Base class 
class A:
	def func1(self):
		print("This is A class.")

# Hierarchical inheritance, both B and C Classes inherit from A Class
class B(A):
	def func2(self):
		print("This is B class.")
		
class C(A):
	def func3(self):
		print("This is C class.")
		
# Multilevel inheritance, class D inherit from B class which is inherit from A Class
class  D(B):
	def func3(self):
		print("This is C class.")

def main():
  obj0 = B()
  obj0.func1()
  obj1 = D()
  obj1.func1()

if __name__ == '__main__':
  main()