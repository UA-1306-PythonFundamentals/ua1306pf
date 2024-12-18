from math import pow, pi

def area_of_rectangle():
    w, l = int(input('enter a width ')), int(input('enter a length '))
    result = w * l
    return f'Area of rectangle: {result}'


def area_of_triangle():
    b, h = int(input('Enter a base ')), int(input('Enter a height '))
    result = 1 / 2 * b * h
    return f'The area_of_triangle is: {result}'


def area_of_circle():
    r = int(input('Enter a radius '))
    result = round(pi * (pow(r, 2)), 2)
    return f'The area_of_circle is: {result}'