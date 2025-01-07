class Employee:
    """
    Employee tracker.
    Parameters:
        name (str): Name and Surname
        salary (int): Salary in USD
    """
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def total_num(cls):
        print(f'Total employees: {cls.counter}')

    def info(self):
        print(f'Employee Name: {self.name}\nEmployee Salary: ${self.salary}')


e_1 = Employee(name='Jessica A', salary=2888)
e_1.info()
e_1.total_num()

e_2 = Employee(name='Gustavo N', salary=1829)
e_2.info()
e_2.total_num()

print('Parent: ', Employee.__base__)
print('Namespace: ', Employee.__dict__)
print('Class Name: ', Employee.__name__)
print('Module Name: ', Employee.__module__)
print('Documentation: ', Employee.__doc__)
