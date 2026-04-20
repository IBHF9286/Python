#abstract class are classes that cannot be instantiated. They are meant to be subclassed or in layman terms they are meant to be inherited by child classes. They help to create a blueprint for other classes. They can contain abstract methods which are methods that are declared but not implemented. The child classes that inherit from the abstract class must implement the abstract methods. 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  
    @abstractmethod
    def stop_engine(self):
        pass 

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")
    def stop_engine(self):
        print("Motorcycle engine stopped")

class Truck(Vehicle):
    def start_engine(self):
        print("Truck engine started")
    def stop_engine(self):
        print("Truck engine stopped")

class Boat(Vehicle):
    def start_engine(self):
        print("Boat engine started")
    def stop_engine(self):
        print("Boat engine stopped")

#if we forget to implement the abstract methods in the child class, we will get an error.

car = Car()
car.start_engine()
car.stop_engine()

motorcycle = Motorcycle()
motorcycle.start_engine()
motorcycle.stop_engine()

truck = Truck()
truck.start_engine()
truck.stop_engine()

boat = Boat()
boat.start_engine()
boat.stop_engine()

