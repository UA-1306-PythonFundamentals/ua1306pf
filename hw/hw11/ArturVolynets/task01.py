# 1. Write a program that prompts the user to enter their age, 
# and then displays a message stating whether the age is even or odd. 
# The program must provide the ability to enter a negative number, 
# and in this case generate an exception. The master code
# should call a function that processes the information entered.

class WrongAgeError(Exception):
    """Exception for handling wrong age errors."""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self) -> str:
        return f"Error: {self.message}"

def process_age(age):
    """Process the provided age to check if it's negative or even/odd."""
    if age < 0:
        raise WrongAgeError("Age cannot be negative")
    if age % 2 == 0:
        print(f"Your age ({age} years) is even.")
    else:
        print(f"Your age ({age} years) is odd.")

try:
    age = int(input("Enter your age: "))
    process_age(age)
except WrongAgeError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

