#createing a base class called Vehicle
class Vehicle:
  def displayVehicle(self):
    return f'This is a Vehicle class'

#createing a derived class from Vehicle class named Car
class Car(Vehicle):
  def displayCar(self):
    return f'This is a Car class'

#createing a derived class from Car class named Bus
class Bus(Car):
  def displayBus(self):
    return f'This is a Bus class'


def main():
 v1 = Vehicle()
 print(v1.displayVehicle())
 print("*****************")
 #The object of derived class can access to method in base class
 c1 = Car()
 print(c1.displayCar())
 print(c1.displayVehicle())
 print("*****************")
 b1 = Bus()
 print(b1.displayBus())
 print(b1.displayVehicle())
 print(b1.displayCar())

 
if __name__ == '__main__':
  main()
  
  