class Employee:
 
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name  # Ім'я співробітника
        self.salary = salary  # Заробітна плата співробітника
        Employee.total_employees += 1  # Лічильник збільшується при створенні нового співробітника

    @classmethod
    def display_total_employees(cls):
        """Метод для виведення загальної кількості співробітників"""
        print(f"Загальна кількість співробітників: {cls.total_employees}")

    def display_employee_info(self):
        """Метод для відображення інформації про співробітника"""
        print(f"Ім'я: {self.name}, Заробітна плата: {self.salary}")


employee1 = Employee("Олександр", 25000)
employee2 = Employee("Марія", 30000)
employee3 = Employee("Іван", 28000)
employee4 = Employee("Наталія", 32000)
employee5 = Employee("Олег", 27000)


employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()
employee4.display_employee_info()
employee5.display_employee_info()


Employee.display_total_employees()
