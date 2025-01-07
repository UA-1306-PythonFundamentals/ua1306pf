class Person:
    
    def __init__(self, name):
        self.name = name

    # Метод, який відображає вітальне повідомлення
    def greet(self):
        return f"Привіт, {self.name}! Раді бачити тебе."

    # Метод класу, що повертає інформацію про вид
    @classmethod
    def species_info(cls):
        return "Це вид: Homosapiens."

    # Статичний метод, який повертає довільне повідомлення
    @staticmethod
    def random_message():
        return "gakgl;ajsklf;klajff"


if __name__ == "__main__":
    # Створення екземпляра класу
    person1 = Person("Олександр")
    
    # Виклик методу greet
    print(person1.greet())

    # Виклик методу класу species_info
    print(Person.species_info())

    # Виклик статичного методу random_message
    print(Person.random_message())
