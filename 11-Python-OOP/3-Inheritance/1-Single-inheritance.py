# single inheritance
# Base class
class A:
	def func1(self):
		print("This is A class.")

# Derived class
class B(A):
	def func2(self):
		print("This is B class.")


def main():
  obj0 = B()
  obj0.func1()
  obj0.func2()

if __name__ == '__main__':
  main()
