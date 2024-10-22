class Employees:
  def __init__(self, name, Id):
    self.__name = name 
    self.__Id = Id
  #Make get and set functions to each attribute
  #Setting methods
  def set_name(self, name):
    self.__name = name 
  def set_Id(self, Id):
    self.__Id = Id
  
  #Getting methods
  def get_name(self):
    return self.__name
  def get_Id(self):
    return self.__Id
  
  #Deleting value
  def del_name(self):
    del self.__name
    return print("The name is deleted")
  
  def del_Id(self):
    del self.__Id
    return print("The ID is deleted")
  ##Encapsulation the private attributes by property method 
  Name = property(get_name, set_name,del_name,"name")
  ID = property(get_Id, set_Id,del_Id, "Id")
    

def main():
  employee1 = Employees("Nora", 123)
  #Access to private variables via property method
  print("Employee name is", employee1.Name)
  print("Employee ID is", employee1.ID)
  print("------Try change values -------")
  employee1.Name = "Sara"
  employee1.ID = 111
  print("Employee name is", employee1.Name)
  print("Employee ID is", employee1.ID)
 #Deleting value 
  del employee1.Name
  del employee1.ID
  
if __name__ == '__main__':
  main()
  