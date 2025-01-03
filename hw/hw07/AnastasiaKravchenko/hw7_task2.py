import math


def rectangle_area(width, length):
    """
    Calculates rectangle area.
    Parameters:
        width (float): side 1 of rectangle
        length (float): side 2 of rectangle
    Returns:
        float: area
    """
    return width * length


def triangle_area(base, height):
    """
    Calculates triangle area.
    Parameters:
        base (float): triangle base side
        height (float): triangle perpendicular height
    Returns:
        float: area
    """
    return round((base * height) / 2, 1)


def circle_area(r):
    """
    Calculates circle area.
    Parameters:
        r (float): radius
    Returns:
        float: area
    """
    return round(r**2 * math.pi, 1)


user_choice = input('Which shape area would you like to calculate?\n')
if user_choice == 'rectangle':
    user_width = input('Enter width: ')
    user_length = input('Enter length: ')
    print(f'The area of a rectangle is: {rectangle_area(float(user_width), float(user_length))}')
elif user_choice == 'triangle':
    user_base = input('Enter base: ')
    user_height = input('Enter height: ')
    print(f'The area of triangle is: {triangle_area(float(user_base), float(user_height))}')
elif user_choice == 'circle':
    user_radius = input('Enter radius: ')
    print(f'The area of a circle is: {circle_area(float(user_radius))}')
else:
    print('I don\'t know such shape.')

