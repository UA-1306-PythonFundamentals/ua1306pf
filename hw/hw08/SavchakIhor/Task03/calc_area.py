from math import pow, pi


def area_rectangle(a, b):
    """Functions calculates an area of rectangle"""
    area = a * b 
    return area


def area_triangle(b, h):
    """Functions calculates an area of triangle"""
    area = 1/2 * (b * h)
    return area


def area_circle(r):
    """Functions calculates an area of circle"""
    area = round(pi * pow(r, 2), 2)
    return area
