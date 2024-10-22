from multipledispatch import dispatch
class Addition:
   @dispatch(int, int)
   def Add(self, a, b):
      x = a + b
      return x
   @dispatch(int, int, int)
   def Add(self, a, b, c):
      x = a + b + c
      return x
def main():
   obj = Addition()

   print (obj.Add(1,2,3))
   print (obj.Add(4,5))
if __name__ == '__main__': 
    main()