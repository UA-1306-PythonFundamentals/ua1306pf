# import water_state

# def main():
#     try:
        
#         temperature = float(input("Enter the temperature of water in degrees: "))
        
        
#         water_state.print_water_state(temperature)
#     except ValueError:
#         print("Please enter a valid number.")

# if __name__ == "__main__":
#     main()


# def parse_login(login):

#     login = login.lower()

#     if "-id" in login:
#         parts = login.split("-id")
#     elif "id" in login:
#         parts = login.split("id")
#     elif "-" in login:
#         parts = login.split("-")
#     else:
     
#         raise ValueError(f"incorrect login '{login}'")
   
#     return parts


class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        """This method should be overridden in subclasses."""
        return "Generic animal sound"

# Mammal subclass
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} gives birth to live young."

    def make_sound(self):
        return "Roar"

# Bird subclass
class Bird(Animal):
    def lay_eggs(self):
        return f"{self.name} lays eggs."

    def make_sound(self):
        return "Squawk"

# Reptile subclass
class Reptile(Animal):
    def shed_skin(self):
        return f"{self.name} sheds its skin."

    def make_sound(self):
        return "Hiss"

# Example usage
if __name__ == "__main__":
    # Create instances of each subclass
    lion = Mammal("Lion", "Mammals", 4)
    eagle = Bird("Falcon", "Bird", 2)
    snake = Reptile("Python", "Reptile", 4)

    # Test Mammal
    print(f"Animal: {lion.name}, Species: {lion.species}, Legs: {lion.legs}, Sound: {lion.make_sound()}")
 

    # Test Bird
    print(f"Animal: {eagle.name}, Species: {eagle.species}, Legs: {eagle.legs}, Sound: {eagle.make_sound()}")


    # Test Reptile
    print(f"Animal: {snake.name}, Species: {snake.species}, Legs: {snake.legs}, Sound: {snake.make_sound()}")
