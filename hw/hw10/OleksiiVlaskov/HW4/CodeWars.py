#1
class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type
#2
import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white","yellow","purple","red"])
#3
def God():
    return [Man(), Woman()]

class Human:
    pass

class Woman(Human):
    pass

class Man(Human):
    pass
#4
class Person:
    def __init__(self,name,age):
        self.name = str(name)
        self.age = int(age)
        self.info=f"{self.name}s age is {self.age}"
#5
import math
import math
class Sphere(object):
    def __init__(self,radius,mass):
        self.radius=float(radius)
        self.mass=float(mass)
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(math.pi * self.radius**3 * 4/3, 5)
    
    def get_surface_area(self):
        return round(4 * math.pi * self.radius**2, 5)
    
    def get_density(self):
        return round(self.mass / (math.pi * self.radius**3 * 4/3), 5)
#6
def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception