#nested classes

class Company():
    
    class Employee():
        def __init__(self, employee_name, position):
            self.employee_name = employee_name
            self.position = position

        def get_details(self):
            return f"{self.employee_name} works as {self.position}"

    def __init__(self, name):
        self.name = name
        self.employee_list = []

    def  add_employee(self, employee_name, position):
        employee = self.Employee(employee_name, position)
        self.employee_list.append(employee)

    def get_employees(self):
        return [employee.get_details() for employee in self.employee_list]
    
company1 = Company("Tech Solutions")
company1.add_employee("Alice", "Software Engineer")
company1.add_employee("Bob", "Data Scientist")
print(f"Employees at {company1.name}:")
for employee_details in company1.get_employees():
    print(employee_details)

company2 = Company("Creative Agency")
company2.add_employee("Charlie", "Graphic Designer")
company2.add_employee("Diana", "Content Writer")
print(f"Employees at {company2.name}:")
for employee_details in company2.get_employees():
    print(employee_details)
