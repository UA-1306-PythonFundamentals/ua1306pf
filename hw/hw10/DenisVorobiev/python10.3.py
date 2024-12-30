class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @staticmethod
    def total_employees():
        return f"Employee: {Employee.employee_count}"

    def display_info(self):
        print(f"Name: {self.name}, Fee: {self.salary}")

    # Вывод информации о классе:
    def class_info():
        print("base:", Employee.__base__)
        print("dict:", Employee.__dict__)
        print("name:", Employee.__name__)
        print("module:", Employee.__module__)
        print("doc:", Employee.__doc__)

# Пример использования:
emp1 = Employee("A", 50000)
emp2 = Employee("B", 60000)

emp1.display_info()
emp2.display_info()
print(Employee.total_employees())