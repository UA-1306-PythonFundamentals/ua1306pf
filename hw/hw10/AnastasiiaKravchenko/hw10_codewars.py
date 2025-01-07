# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# Color Ghost
import random

class Ghost(object):
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)


# Basic subclasses - Adam and Eve
def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]


class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()


# Classy Classes
class Person:
    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"


# Building Spheres
import math


class Sphere(object):
    def __init__(self, radius: [int, float], mass: [int, float]):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


# Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if not (new_name[0].isupper() and new_name.isalnum()):
        raise Exception('Wrong class name')

    cls.__name__ = new_name
