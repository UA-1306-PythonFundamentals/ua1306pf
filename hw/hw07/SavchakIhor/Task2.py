def area_choice():
    """Calculates the area of a rectangle, triangle, or circle based on user choice."""
    shape = input("Please choose a shape (rectangle, triangle, or circle): ").lower()

    if shape == 'rectangle':
        width = float(input('Enter the width: '))
        length = float(input('Enter the length: '))
        result = width * length
        print(f'The area of the rectangle is: {result}')

    elif shape == 'triangle':
        base = float(input('Enter the base: '))
        height = float(input('Enter the height: '))
        result = 0.5 * base * height
        print(f'The area of the triangle is: {result}')

    elif shape == 'circle':
        radius = float(input('Enter the radius: '))
        pi = 3.14159  # More accurate value for PI
        result = pi * radius ** 2
        print(f'The area of the circle is: {result}')

    else:
        print("Invalid shape. Please choose rectangle, triangle, or circle.")


area_choice()
