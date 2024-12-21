#Task 1
class Ball:
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

#Task 2

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

#Task3
class Human:
    pass

class Woman(Human):
    pass

class Man(Human):
    pass

#Task4
class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age  = int(age)
        self.info = f"{self.name} age is {self.age}"

#Task5
from math import pi

class Sphere:
    def __init__(self, radius, mass):
        self.radius = float(radius)
        self.mass = float(mass)

    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round((4/3 * pi * self.radius**3), 5)
    
    def get_surface_area(self):
        return round((4 * pi * self.radius**2), 5)
    
    def get_density(self):
        return round((self.mass / (4/3 * pi * self.radius**3)), 5)
    

