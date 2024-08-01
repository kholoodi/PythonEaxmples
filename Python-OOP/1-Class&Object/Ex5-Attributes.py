class Employees:
  #Declareing the "employee_count" as class attributes
  employee_count = 0
  
  def __init__(self,**kwargs):
    #The "kwargs" is an instance attribute
    self.Data = kwargs
    
    #Access to class attributes by class name
    Employees.employee_count += 1 #make change on class attribute value
    
  def GetEmployees(self):
    print("The info of Employee",Employees.employee_count,"is:")
    for x,y in self.Data.items():
      print(x ,":", y)
    print("\n")
    
    
def main():
  employee1 = Employees(Name ="Nora", employee_id=111, Department="HR", Salary= 12000) 
  employee1.GetEmployees()
  
  employee2 = Employees(Name= "Sara", employee_id=221, Department= "IT",Salary= 20000)
  employee2.GetEmployees()
  
  employee3 = Employees(Name= "Reem", employee_id=331, Department= "PR",Salary= 15000)
  employee3.GetEmployees()
  
  #Class attributes can be accessed by both class name and object name.
  print("The number of Employees is:", employee2.employee_count)
  
if __name__ == '__main__':
  main()
  