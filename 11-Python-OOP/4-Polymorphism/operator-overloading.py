class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"

#Create an operator for sum two points
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
def main():
  #Creating two Point objects
  point1 = Point(1, 2)
  point2 = Point(3, 4)

  # Adding two Point objects using the overloaded '+' operator
  print( point1 + point2) # Output: (4, 6)

if __name__ == '__main__': 
    main()
