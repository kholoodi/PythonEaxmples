class Students:
  student_count = 0
  def __init__(self,Name , CoursesNo):
    self.Name = Name
    self.CoursesNo = CoursesNo
    Students.student_count += 1 
  
   
  def StudentCount():
    print("Student Number is :", Students.student_count)
    #A static method
  Stcounter = staticmethod(StudentCount)
    
def main():
  st1 = Students(Name ="Nora", CoursesNo= 6) 
  st2 = Students(Name= "Sara", CoursesNo= 5)
  st3 = Students(Name= "Reem", CoursesNo= 7)

  #clalling the static method  vis class 
  Students.Stcounter()
  #calling the static method via object  
  st2.Stcounter()
  
if __name__ == '__main__':
  main()
  