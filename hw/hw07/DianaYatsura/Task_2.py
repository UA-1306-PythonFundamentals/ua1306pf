def area_choice():
    shape = input("Please, choose and enter a shape: rectangle, triangle or circle ")
    if shape == 'rectangle':
        def area_of_rectangle():
            w, l = int(input('enter a width ')), int(input('enter a length '))
            result = w * l
            return result
        print(f'The area_of_rectangle is: {area_of_rectangle()}')
    elif shape == 'triangle':
        def area_of_triangle():
            b, h = int(input('Enter a base ')), int(input('Enter a height '))
            result = 1 / 2 * b * h
            return result
        print(f'The area_of_triangle is: {area_of_triangle()}')
    elif shape == 'circle':
        def area_of_circle():
            PI = 3.14
            r = int(input('Enter a radius '))
            result = PI * r ** 2
            return result
        print(f'The area_of_circle is: {area_of_circle()}')


area_choice()