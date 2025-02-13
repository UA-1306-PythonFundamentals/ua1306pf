class Employee:
    """
    Represents an employee with their name, salary, and a class-level employee counter.
    """

    employee_counter = 0  # Class variable to track the total number of employees

    def __init__(self, name: str, salary: float):
        """Initializes the employee with a name and salary."""
        self.name = name
        self.salary = salary
        Employee._increment_employee_counter()

    def __del__(self):
        """Decrements the employee counter when an employee is removed."""
        Employee._decrement_employee_counter()

    @classmethod
    def _increment_employee_counter(cls):
        """Private helper method to increment the employee counter."""
        cls.employee_counter += 1

    @classmethod
    def _decrement_employee_counter(cls):
        """Private helper method to decrement the employee counter."""
        cls.employee_counter -= 1

    @classmethod
    def get_employee_count(cls):
        """Class method to return the current number of employees."""
        return cls.employee_counter

    def display_details(self):
        """Displays detailed information about the employee."""
        print(f"--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"------------------------")

# Creating employee instances
employee1 = Employee("Artur", 10000)
employee2 = Employee("Alice", 15000)

# Displaying employee details
employee1.display_details()
employee2.display_details()

# Checking total number of employees
print(f"Total Employees: {Employee.get_employee_count()}")

# Deleting one employee
del employee1

# Checking total employees after deletion
print(f"Total Employees after deletion: {Employee.get_employee_count()}")

# Displaying class metadata
print("\n--- Class Metadata ---")
print(f"Parent Class: {Employee.__base__}")
print(f"Class Dictionary: {Employee.__dict__}")
print(f"Class Name: {Employee.__name__}")
print(f"Module Name: {Employee.__module__}")
print(f"Attributes and Methods: {dir(Employee)}")
print("------------------------")
