class Employee:

    """A class included employees names and salaries, also represent the total number of employees"""

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name.capitalize() if isinstance(name, str) else 'Unknown'
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_employee(cls):
        print(f'The total number of employees is: {Employee.employee_count}')

    def employee_info(self):
        print(f'Name: {self.name}\nSalary: {self.salary}')

print(f'Base class: {Employee.__base__}')
print(f'Class namespace: {Employee.__dict__}')
print(f'Class name: {Employee.__name__}')
print(f'Module name: {Employee.__module__}')
print(f'Docstring: {Employee.__doc__}')


a = Employee('henry', 2300)
a.employee_info()
b = Employee('cat', 344)
b.employee_info()
c = Employee('arny', 45556)
c.employee_info()
Employee.total_employee()