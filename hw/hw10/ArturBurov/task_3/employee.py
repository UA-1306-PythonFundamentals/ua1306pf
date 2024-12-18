class Employee:
    total_employees = 0  # Class variable to count the total number of employees

    def __init__(self, name, salary):
        self.name = name  # Instance variable for employee's name
        self.salary = salary  # Instance variable for employee's salary
        Employee.total_employees += 1  # Increment the employee counter

    @classmethod
    def display_employee_count(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


employee1 = Employee("Sergey Popov", 50000)
employee2 = Employee("Irina Cvetkova", 60000)
employee3 = Employee("Oleg Ivanov", 55000)

employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()

Employee.display_employee_count()  # Accessing through a class

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
