from math import pow, pi

def area_rectangle(length, width):
    """Given the length and width of a rectangle, return the area of the rectangle"""
    result = round(length * width, 2)
    return result

def area_triangle(base, p_height):
    """Given the base of the triangle and the perpendicular height, return the area of the triangle"""
    result = round(base * p_height * 0.5, 2)
    return result    

def area_circle(radius):
    """Given the radius of a circle, find the area of the circle"""
    result = round(pi * pow(radius, 2), 2)
    return result