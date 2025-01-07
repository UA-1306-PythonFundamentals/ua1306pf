class Employee:
    """
    Class represents an employee with basic details and a class-wide employee counter.
    """

    employee_counter = 0

    def __init__(self, name, salary):
        """Initializes the employee object with name and salary."""
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1

    def __del__(self):
        """Decrements the employee counter when an employee object is deleted."""
        Employee.employee_counter -= 1

    @classmethod
    def print_employees_count(cls):
        """Class method to print the total number of employees."""
        print(f"The total employees count is {cls.employee_counter}")

    def display_info(self):
        """Displays detailed information about the employee."""
        print(f"---------- Employee Info ----------")
        print(f"Name:   {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"-----------------------------------")

employee1 = Employee("Artur", 10000)
employee2 = Employee("Alice", 15000)

employee1.display_info()
employee2.display_info()

Employee.print_employees_count()

del employee1

Employee.print_employees_count()

print("\n------ Class Metadata ------")
print(f"Parental class: {Employee.__base__}")
print(f"Class dictionary: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Available attributes and methods: {dir(Employee)}")
print("-----------------------------")

