from math import pow, pi


def rectangle_area(a, b):
    """
    Calculates the area of rectangle: S = a * b
    Parameters:
        a (float | int): first side
        b (float | int): second side
    Returns:
        float: area
    """
    return round(a * b, 1)


def triangle_area(a, h):
    """
    Calculates the area of triangle: S = 0.5 * a * h
    Parameters:
        a (float | int): side
        h (float | int): height
    Returns:
        float: area
    """
    return round(0.5 * a * h, 1)


def circle_area(r):
    """
    Calculates the area of circle: S = pi * r ** 2
    Parameters:
        r (float | int): radius
    Returns:
        float: area
    """
    return round(pi * pow(r, 2), 1)
