class Employees:
  def __init__(self, name, Id, salary):
    self.name = name #public variable
    self.__Id = Id #private variable
    self._salary = salary # protected variable
  
  #Access for instance variables via instance method 
  def GetEmployees(self):
    print("Employee Name:", self.name)
    print("Employee ID:", self.__Id)
    print("Salary:", self._salary)
    
def main():
  employee1 = Employees("Nora", 123, 12000)
  #Can access to values of private and protected variables via instance method
  employee1.GetEmployees()
  print(employee1._salary)
  #Can't access to values of private variables from out of their class
  #print(employee1.__Id)
  
  
if __name__ == '__main__':
  main()
  