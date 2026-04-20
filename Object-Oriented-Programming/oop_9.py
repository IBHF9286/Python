#static methods: These methods are not bound to the class or instance. They can be called on the class itself without creating an instance. They are defined using the @staticmethod decorator.

class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} works as a {self.position}"
    
    @staticmethod
    def company_info():
        return "This is a company that values its employees."
    
    @staticmethod
    def available_positions(position):
        positions = ["Data Scientist","Cook","Manager","Worker"]
        return position in positions
    
# callling instance methods
 
emp1 = Employee("Alice", "Data Scientist")    
emp2 = Employee("Bob", "Cook")
print(emp1.get_info())  # Output: Alice works as a Data Scientist
print(emp2.get_info())  # Output: Bob works as a Cook

# calling static methods
print(Employee.company_info())  # Output: This is a company that values its employees.

position_list = ["Data Analyst", "Cook", "Ex-Army", "Manager", "Principal", "Worker", "Data Scientist"]

for position in position_list:
    print(Employee.available_positions(position))

    