class Human:

    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f"We are glade to see you again {self.name}"
    
    @classmethod
    def species(cls):
        return 'This species is Homosapience', cls
    
    @staticmethod
    def arbutrary_mess():
        return 'This is OOP lesson'
    

person1 = Human("Jon")

print(person1.greetings())
print(person1.species())
print(person1.arbutrary_mess())