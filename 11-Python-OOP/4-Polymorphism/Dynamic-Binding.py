class AnimalsSounds:
  def Sound(self):
    print ("Sound")
    return

class Cat(AnimalsSounds):
  def Sound(self):
    print ("Meow")
    return

class Dog(AnimalsSounds):
  def Sound(self):
    print ("Woof")
    return

def main():
  Sounds = [Cat(), Dog()]
  for animal in Sounds:
    animal.Sound()
  
if __name__ == '__main__': 
    main()