class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def employee_count(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e = Employee("Oleksandra", 12000)
e.employee_info()
Employee.employee_count()  

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation bar:", Employee.__doc__)

