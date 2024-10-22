from abc import ABC, abstractmethod
# creating interface
class ourInterface(ABC):
   @abstractmethod
   def WelcomMessage(self):
      pass

   @abstractmethod
   def NumMuiMltiplier(self):
      pass

# class implementing the above interface
class interface1(ourInterface):
   def WelcomMessage(self):
      print ("Welcome to  Interface 1")
      return
   
   def NumMuiMltiplier(self,x):
      return x *2
# class implementing the above interface
class interface2(ourInterface):
   def WelcomMessage(self):
      print ("Welcome to  Interface 2")
      return
   
   def NumMuiMltiplier(self,x):
      return x *3
def main():  
   #creating instances     
   obj1 = interface1()
   obj1.WelcomMessage()
   print (obj1.NumMuiMltiplier(3))

   #creating instances     
   obj2 = interface2()
   obj2.WelcomMessage()
   print (obj2.NumMuiMltiplier(3))

if __name__ == '__main__': 
    main()