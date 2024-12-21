from area import *


shape = input('Which shape you want the area for?\n')
if shape == 'rectangle':
    side1 = float(input('Enter first side of rectangle: '))
    side2 = float(input('Enter second side of rectangle: '))
    print(f'Area is: {rectangle_area(side1, side2)}')
elif shape == 'triangle':
    side = float(input('Enter side of triangle: '))
    height = float(input('Enter height of triangle: '))
    print(f'Area is: {triangle_area(side, height)}')
elif shape == 'circle':
    radius = float(input('Enter radius of circle: '))
    print(f'Area is: {circle_area(radius)}')
else:
    print('Unknown shape')
