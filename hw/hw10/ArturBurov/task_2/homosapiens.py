class Human:
    species = "Homosapiens"  # Class variable representing the species

    def __init__(self, name):
        self.name = name  # Instance variable representing the name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This is a species of '{cls.species}'"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message from the Human class."


person1 = Human("Tatyana")
person2 = Human("Semen")

person1.welcome_message()
person2.welcome_message()

print(person1.get_species())  # Output: This is a species of 'Homosapiens'

print(person1.arbitrary_message())  # Output: This is an arbitrary message from the Human class.
