class Students():

    #class variable: These are the variables that are shared among all the instances of a class. They are defined within the class but outside of any method. They are accessed using the class name or through an instance of the class.

    class_year = 2026
    num_students = 0

    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.num_students += 1

student1 = Students("Alice", 20)
student2 = Students("Bob", 21)
student3 = Students("Charlie", 22)
student4 = Students("David", 23)

#accessing class variables 
print(f"My class of graduating year {Students.class_year} has {Students.num_students} students.")

#accessing instance variables
print(f"{student1.name} is {student1.age} years old.")
print(f"{student2.name} is {student2.age} years old.")
print(f"{student3.name} is {student3.age} years old.")
print(f"{student4.name} is {student4.age} years old.")

