class Students:
  student_count = 0
  
  def __init__(self,**kwargs):
    self.Data = kwargs
    Students.student_count += 1 
    
  #An instance method
  def StudentCount(self):
    print("Student Number is :", self.student_count)
    
  #A class method
  StCounter = classmethod(StudentCount)
    
def main():
  st1 = Students(Name ="Nora", CoursesNo= 6) 
  st2 = Students(Name= "Sara", CoursesNo= 5)
  st3 = Students(Name= "Reem", CoursesNo= 7)

  #calling the instance method
  st2.StudentCount()
  #clalling the class method 
  Students.StCounter()
if __name__ == '__main__':
  main()
  