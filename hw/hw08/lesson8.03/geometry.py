import math

def rectangle_area(a, b):
    """Обчислення площі прямокутника."""
    return a * b

def triangle_area(h, a):
    """Обчислення площі трикутника."""
    return 0.5 * h * a

def circle_area(r):
    """Обчислення площі кола."""
    return math.pi * math.pow(r, 2)
