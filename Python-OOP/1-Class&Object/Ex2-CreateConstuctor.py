class Employees:
  #create the constuctor 
  def __init__(self, name):
    self.name = name
  
  def GetEmployees(self):
    print("The employee name is", self.name)
    

def main():
  #Create the frist instance to the Employees class  
  employee1 = Employees("Nora") #calling the constuctor
  employee1.GetEmployees()
  
  #Create the second instance 
  employee2 = Employees("Sara")
  employee2.GetEmployees()

if __name__ == '__main__':
  main()
  