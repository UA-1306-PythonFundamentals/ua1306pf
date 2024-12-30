# Task2. Create a class Human, everyone has a name, create a method in the class 
# that displays a welcome message to each person. Create a class method in the class 
# that returns information that it is a species of "Homosapiens". 
# And in the class create a static method that returns an arbitrary message.

class Human:
    '''
    Class representing a human with a name and basic methods.
    '''
    def __init__(self, name):
        '''
        Initializes the Human instance with a name.
        
        :param name: The name of the human.
        '''
        self.name = name

    def greeting(self):
        '''
        Prints a welcome message with the person's name.
        '''
        print(f"Hello, {self.name}!")
    
    @classmethod
    def species(cls):
        '''
        Class method that displays the species of the human.
        '''
        print(f"The species is homosapiens.")

    @staticmethod
    def message():
        '''
        Static method that returns an arbitrary message.
        '''
        print("message :)")



human = Human("Artyr")
human.greeting()
human.species()
human.message()
