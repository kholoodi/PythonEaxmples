class Organization:
  def __init__(self):
    #The inner classes are attribute 
    self.Fin = self.Finance()
    self.market = self.Marketing()
  
  def organization(self):
    print("This an Organization class")
    
  #An inner class
  class Finance:
    def finance(self):
      print("This is Finance Department")
  
  #An inner class  
  class Marketing:
    def marketing(self):
      print("This is Marketing Department")
    

def main():
  # instance of OuterClass
  Org = Organization()
  Org.organization()
  
  #Instance of innerClasses
  Fin = Org.Fin
  Fin.finance()
  
  market = Org.market
  market.marketing()
  
if __name__ == '__main__':
  main()
  