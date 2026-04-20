class Car():

    def __init__(self, model, year, color):
        #this is the constructor method, it is called when we create an object of the class. It initializes the attributes of the object.
        self.model = model
        self.year  = year
        self.color = color

    def start_engine(self):
        #this is a method of the class, it can be called on an object of the class.
        print(f"{self.model} engine is starting...")

    def stop_engine(self):
        #this is another method of the class, it can be called on an object of the class.
        print(f"{self.model} engine is stopping...")

car1 = Car("Mustang", 2026, "Blue")
#car1 is an object of the class Car. We can access the attributes of the object using the dot notation.
print(car1.model)
print(car1.year)
print(car1.color)

car2 = Car("Camaro", 2025, "Red")
car3 = Car("Challenger", 2024, "Black")

#we can also call the methods of the class on the objects.
car2.start_engine()
car3.stop_engine()

#difference between __init__ and other methods:
#1. __init__ is a special method that is called when an object of the class is created. This method is not called explicitly, it is called automatically when we create an object of the class. Other methods are called explicitly on the object of the class.
#2. __init__ is used to initialize the attributes of the object, while other methods are used to perform some actions on the object or to return some values based on the attributes of the object.

