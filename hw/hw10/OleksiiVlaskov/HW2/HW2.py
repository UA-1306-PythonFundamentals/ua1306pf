class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome(self):
        return f"Welcome {self.name}. Glad to see you!"
    
    @classmethod
    def species(cls):
        return f"{cls.__name__} is a species of Homosapiens"
    
    @staticmethod
    def arbitrary():
        return f"Hey there, it's a beautiful day outside, isn't it"
    
Arnold = Human('Arnold')

print(Arnold.welcome())
print(Human.species())
print(Human.arbitrary())
print(Arnold.arbitrary())