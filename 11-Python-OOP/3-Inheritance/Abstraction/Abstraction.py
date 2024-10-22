# Python Abstraction
# Import required modules
from abc import ABC, abstractmethod
# Crate abstract class as a base class, and it is must inhert from ABC  
class A(ABC):
  # Create abstract method      
  @abstractmethod
  def func(self):
    pass

# Derived class 1
class B(A):
	def func(self):
		print("This is B class.")
		
# Derived class 2
class C(A):
	def func(self):
		print("This is C class.")

def main():
 obj0 = B()
 obj0.func()
 obj1 = C()
 obj1.func()
 
if __name__ == '__main__':
  main()