class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"
    
def main():
    def make_sound(animal):
        print(animal.sound())

    cat = Cat()
    dog = Dog()

    make_sound(cat)  # Output: Meow
    make_sound(dog)  # Output: Woof

if __name__ == '__main__': 
    main()