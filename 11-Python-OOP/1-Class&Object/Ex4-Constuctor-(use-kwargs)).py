class Employees:
  def __init__(self,**kwargs):
    self.Data = kwargs
  
  def GetEmployees(self):
    print("The Employee info:")
    for x,y in self.Data.items():
      print(x ,":", y)
    print("\n")
    
    
def main():
  employee1 = Employees(name ="Nora", employee_id=123, department="HR", salary= 12000) 
  employee1.GetEmployees()
  
  employee2 = Employees(name= "Sara", employee_id =321, department= "IT",salary= 20000)
  employee2.GetEmployees()

if __name__ == '__main__':
  main()
  