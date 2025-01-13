class Human:
    '''
    A class representing a human, their name, and some basic actions.
    '''
    species = "Homo sapiens"  # Class variable for species

    def __init__(self, name: str):
        '''
        Initializes the Human instance with a name.

        :param name: The name of the human.
        '''
        self.name = name

    def greeting(self):
        '''
        Prints a personalized greeting with the human's name.
        '''
        print(f"Hello, my name is {self.name}.")

    def species_info(self):
        '''
        Prints the species of the human (using the class variable).
        '''
        print(f"I am a {self.species}.")

    @staticmethod
    def message(msg: str = "message :)"):
        '''
        Static method that prints any custom message.

        :param msg: The message to display (default is "message :)").
        '''
        print(msg)


# Create an instance of Human
human = Human("Ihor")

# Calling instance methods
human.greeting()
human.species_info()

# Calling static method with custom message
Human.message("Welcome to the Human class!")
