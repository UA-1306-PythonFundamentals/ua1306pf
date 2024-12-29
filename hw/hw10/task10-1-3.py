class Employee:
    total_employees = 0  # Class variable to track the total number of employees

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def total_count(cls):
        return cls.total_employees

    def display_employee(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"
