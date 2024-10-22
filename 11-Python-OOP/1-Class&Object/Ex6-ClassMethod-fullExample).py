class Students:
  student_count = 0
  
  def __init__(self,**kwargs):
    self.Data = kwargs
    
    Students.student_count += 1 
   #An Instance Method 
  def GetStudents(self):
    print("The info of Student",Students.student_count,"is:")
    for x,y in self.Data.items():
      print(x ,":", y)
    print("\n")
  #An Instance Method
  def StudentCount(self):
    print("Student Number is :", self.student_count)
    
  #A class Method
  StCounter = classmethod(StudentCount)
    
    
def main():
  st1 = Students(Name ="Nora", CoursesNo= 6) 
  st1.GetStudents()
  
  st2 = Students(Name= "Sara", CoursesNo= 5)
  st2.GetStudents()
  
  st3 = Students(Name= "Reem", CoursesNo= 7)
  st3.GetStudents()
  #calling the instance method
  st2.StudentCount()
  #clalling the class method 
  Students.StCounter()
if __name__ == '__main__':
  main()
  