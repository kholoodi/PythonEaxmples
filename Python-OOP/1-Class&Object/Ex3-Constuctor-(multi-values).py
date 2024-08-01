class Employees:
  def __init__(self, name, employee_id, department, salary):
    self.name = name
    self.employee_id = employee_id
    self.department = department
    self.salary = salary
  
  def GetEmployees(self):
    print("Employee Name:", self.name)
    print("Employee ID:", self.employee_id)
    print("Department:", self.department)
    print("Salary:", self.salary)
    
def main():
  #Create the instance to the Employees class
  employee1 = Employees("Nora", 123, "HR", 12000) 
  employee1.GetEmployees()
  
  #create the second instance 
  employee2 = Employees("Sara", 321, "IT", 20000)
  employee2.GetEmployees()

if __name__ == '__main__':
  main()
  