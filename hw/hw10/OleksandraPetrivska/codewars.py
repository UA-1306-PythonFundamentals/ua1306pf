#1

class Ball:
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


#2

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
        

#3

def God():
    return Man(), Woman()

class Human:
    pass

class Woman(Human):
    pass

class Man(Human):
    pass


#4

class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age  = int(age)
        self.info = f"{self.name}s age is {self.age}"


#5

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
        return round((4 / 3) * math.pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
    

#6

import re


def class_name_changer(cls, new_name):
    if not new_name:
        raise ValueError("Class name cannot be empty")
    if not re.match(r"^[A-Z][a-zA-Z0-9]*$", new_name):
        raise ValueError(
            "Invalid class name. Must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name

    