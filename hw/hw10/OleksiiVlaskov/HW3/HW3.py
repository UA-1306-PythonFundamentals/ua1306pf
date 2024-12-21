class Employee:
    """An employee class. Each employee has characteristics such as name
and salary. This class have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
name and salary."""

    counter = 0
    employee_name = []
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
        Employee.employee_name.append(self)
    
    @classmethod
    def employee_info(self):
        test = []
        for employee in Employee.employee_name:
            print(f"Salary of employee {employee.name}, is {employee.salary}")
    
    @classmethod    
    def total_empl(self):
        return f"Total number of employees is: {Employee.counter}"
    
        
Alfred = Employee('Alfred', 1000)
print(f"Employee name: {Alfred.name}, {Alfred.salary=}, Employees are: {Employee.counter}")
Barbara = Employee('Barbara', 1500)
print(f"Employee name: {Barbara.name}, {Barbara.salary=}, Employees are: {Employee.counter}")
Conor =  Employee('Conor', 1750)
print(f"Employee name: {Conor.name}, {Conor.salary=}, Employees are: {Employee.counter}")
print(Employee.total_empl())
Employee.employee_info()

print(f"""
{Employee.__base__=}

{Employee.__dict__=}

{Employee.__name__=}

{Employee.__module__=}

{Employee.__doc__=}
""")

