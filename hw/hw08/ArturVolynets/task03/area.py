import math

__all__ = ["rectangle_area", "triangle_area", "circle_area"]

def rectangle_area(a, b):
    """
    Calculate the area of a rectangle.

    Parameters:
    a (float): The length of the rectangle.
    b (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return a * b

def triangle_area(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    a (float): The first side of the triangle.
    b (float): The second side of the triangle.
    c (float): The third side of the triangle.

    Returns:
    float: The area of the triangle if the sides form a valid triangle.
    str: Error message if the sides do not form a valid triangle.
    """
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = pow((p * (p - a) * (p - b) * (p - c)), 0.5)
        return s
    else:
        return "Error! No triangle exists with the given sides."

def circle_area(r):
    """
    Calculate the area of a circle.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * r * r
