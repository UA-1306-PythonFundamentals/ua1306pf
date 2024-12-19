class Employee:

    counter = 0

    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        Employee.counter += 1

    def employee_info(self):
        return f'Employee {self.name} has salary {self.salary}'
    
    @classmethod
    def total_employees(cls):
        return Employee.counter
    

employee1 = Employee("Nata", 100)
employee2 = Employee("Den", 200)
employee3 = Employee("Sviat", 300)

print(employee1.employee_info())
print(employee2.employee_info())
print(employee3.employee_info())

print(Employee.counter)