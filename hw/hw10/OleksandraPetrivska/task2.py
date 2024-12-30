class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f'Welcome, {self.name}!')

    @classmethod
    def species(cls):
        return 'This species is Homosapience'
    @staticmethod
    def arbitrary():
        return "This is an arbitrary message from the Human class."


p = Human("Oleksandra")
p.welcome_message()
print(p.species())  
print(p.arbitrary())  

