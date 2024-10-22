class Employees:
  def __init__(self, name, Id):
    self.__name = name 
    self.__Id = Id
 
 #By using @property to make the variables properties 
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self,name):
    self.__name = name 
  @name.deleter
  def name(self):
    del self.__name
    return print("The name is deleted")

  @property
  def Id(self):
    return self.__Id 
    
  @Id.setter
  def Id(self,Id):
    self.__Id = Id
    
  @Id.deleter
  def Id(self):
    del self.__Id
    return print ("The ID is deleted")


def main():
  employee1 = Employees('Nora', 123)
  #Access to private variables via property method
  print("Employee name is", employee1.name)
  print("Employee ID is", employee1.Id)
  print("------Try change values -------")
  employee1.name = "Sara"
  employee1.Id = 111
  print("Employee name is", employee1.name)
  print("Employee ID is", employee1.Id)
  
  #Delete value 
  del employee1.Id
 
if __name__ == '__main__':
  main()
  