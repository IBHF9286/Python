#multiple inheritance and multilevel inheritance

class animal():
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating food.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class prey(animal):
    def flee(self):
        print(f"{self.name} the prey flees from the predator.")

class predator(animal):
    def hunt(self):
        print(f"{self.name} the predator hunts for prey.")

class rabbit(prey):
    def describe(self):
        print(f"{self.name} the rabbit is a white in color.")

class fox(predator):
    def describe(self):
        print(f"{self.name} the fox is a yellow in color.")

class fish(prey, predator):
    def describe(self):
        print(f"{self.name} the fish is both a prey and a predator.")

#creating objects
rabbit = rabbit("Bunny")
fox = fox("Foxy")
fish = fish("Nemo")

#calling methods

#child class methods
rabbit.describe()
fox.describe()
fish.describe()

#parent class methods
rabbit.flee()
fox.hunt()

fish.flee() #multiple inheritance
fish.hunt() #multiple inheritance

#methods from parent of parent class: Multilevel inheritance

rabbit.eat()
rabbit.sleep()

fox.eat()
fox.sleep()

fish.eat()
fish.sleep()


