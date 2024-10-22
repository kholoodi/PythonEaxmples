class Students:
  student_count = 0
  
  def __init__(self,Name , CoursesNo):
    self.Name = Name
    self.CoursesNo = CoursesNo
    Students.student_count += 1 
    
  #A class method
  @classmethod
  def newStudent(cls,Name,CoursesNo):
    return cls(Name,CoursesNo)
  
  #The second class method
  @classmethod
  def StudentCount(cls):
    print( "The students number is:",cls.student_count)
    
def main():
  st1 = Students(Name ="Nora", CoursesNo= 6) 
  st2 = Students(Name= "Sara", CoursesNo= 5)
  st3 = Students(Name= "Reem", CoursesNo= 7)
  
  #using the class method
  st4 = Students.newStudent("Asma",4)
  
  #clalling the class method 
  Students.StudentCount()
  
if __name__ == '__main__':
  main()
  