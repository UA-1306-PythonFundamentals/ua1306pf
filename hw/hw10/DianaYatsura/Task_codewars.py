# I. Ball-super-ball
class Ball(object):

    def __init__(self, ball_type= 'regular'):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)
print(ball2.ball_type)

# II. Color-ghost
import random

class Ghost(object):

    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost = Ghost()
print(ghost.color)

# III. Basic-subclasses-Adam-and-Eve

class Human:
    pass

class Man(Human):
    def __init__(self):
        self.name = 'Adam'

class Woman (Human):
    def __init__(self):
        self.name = 'Eve'

def God():
    return [Man(), Woman()]

print(God())

# IV. Classy-classes
class Person:

    def __init__(self, name,age):
        self.name = str(name)
        self.age = int(age)
        self.info = f"{name}s age is {age}"

c = Person('Enny', 4)
print(c.info)

# V. Building Spheres

from math import pi

class Sphere(object):

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 4 / 3 * (pi * self.radius ** 3)
        self.surface_area = 4*pi*self.radius**2

    def get_radius(self):
        print(self.radius)

    def get_mass(self):
        print(self.mass)

    def get_volume(self):
        print(round(self.volume,5))

    def get_surface_area(self):
        print(round(self.surface_area, 5))

    def get_density(self):
        print(round((self.mass/self.volume), 5))

ball = Sphere(45.75, 500.44)
ball.get_radius()
ball.get_mass()
ball.get_volume()
ball.get_surface_area()
ball.get_density()

# VI. Dynamic Classes

import re

def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')

class MyClass:
    pass

myObject = MyClass()
print(MyClass.__name__, "MyClass")
class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__, 'UsefulClass')