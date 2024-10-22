class Organization:
  def __init__(self):
    self.Fin = self.Finance()
    
  def organization(self):
    print("This an Organization class")
    
  #An inner class
  class Finance:
    def __init__(self):
      self.count = self.Accounting()
    def finance(self):
      print("This is Finance Department")
  
  #An inner class inside the Finance class
    class Accounting:
      def accounting(self):
        print("This is Accounting Section")
    

def main():
  # instance of Outer Class
  Org = Organization()
  Org.organization()
  
  #Instance of inner Classes
  Fin = Org.Fin
  Fin.finance()
  
  #Instance of inner - inner Classes
  count = Fin.count
  count.accounting()
  

if __name__ == '__main__':
  main()


