# Multilevel inheritance
# Base class 
class A:
	def func1(self):
		print("This is A class.")

# Intermedirctory class
class B(A):
	def func2(self):
		print("This is B class.")
		
# Derived class
class C (B):
	def func3(self):
		print("This is C class.")

def main():
  obj0 = C()
  obj0.func1()
  obj0.func2()
  obj0.func3()

if __name__ == '__main__':
  main()