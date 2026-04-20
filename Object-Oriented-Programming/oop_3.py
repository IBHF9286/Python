#inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

#parent class
class Animal():
    def __init__(self, name):
        self.name = name
        
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


#child classes that inherit from the parent class
class Dog(Animal):
    def sound(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} says: Meow!")

class Mouse(Animal):
    def sound(self):
        print(f"{self.name} says: Squeak!")

dog = Dog("Romi")
cat = Cat("Ginger")
mouse = Mouse("Jerry")


#accessing attributes and methods of the parent class

print(dog.name)  
print(dog.is_alive)
dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()

#accessing methods of the child class

dog.sound()
cat.sound()
mouse.sound()

