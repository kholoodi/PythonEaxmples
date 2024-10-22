#Creat a class and named it "Employees"
class Employees:
  #The frist method in Employees class 
  def SetEmployee(self, name):
    self.name = name
  
  #The second method in Employees class  
  def GetEmployee(self):
    print("The employee name is", self.name)
    

#The main methods
def main():
  
  #Create the frist object (instance) to the Employees class  
  employee1 = Employees()
  #calling the Employees class methods by it's instance 
  employee1.SetEmployee("Nora")
  employee1.GetEmployee()
  
  #Create the second instance 
  employee2 = Employees()
  employee2.SetEmployee("Sara")
  employee2.GetEmployee()

#Calling the main function
if __name__ == '__main__':
  main()
  