#1 Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#2 Color-ghost
import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

#3 Basic-subclasses-Adam-and-Eve
class Human(object):
    # Base class with common attributes or methods for both Man and Woman
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

class Man(Human):
    # Subclass for Man, inherits from Human
    def __init__(self, name="Adam"):
        super().__init__(name)

class Woman(Human):
    # Subclass for Woman, inherits from Human
    def __init__(self, name="Eve"):
        super().__init__(name)

def God():
    # Create Adam (Man) and Eve (Woman) as instances of their respective classes
    adam = Man()
    eve = Woman()
    return [adam, eve]

#4 Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

#5 Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        volume = self.get_volume()
        density = self.mass / volume
        return round(density, 5)

#6 Dynamic Classes
import re

def class_name_changer(cls, new_name):
    # Check if the new name is valid: it should only contain alphanumeric characters
    # and start with an uppercase letter.
    if re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid class name. It must start with an uppercase letter and contain only alphanumeric characters.")
