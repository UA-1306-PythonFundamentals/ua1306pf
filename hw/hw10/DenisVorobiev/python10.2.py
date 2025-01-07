class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def species_info(cls):
        return "homosapiens."

    @staticmethod
    def random_message():
        return "static."

# Пример использования:
person = Human("Human")
person.welcome_message()
print(Human.species_info())
print(Human.random_message())