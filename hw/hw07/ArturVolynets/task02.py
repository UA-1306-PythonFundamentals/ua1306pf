# Task2. Write a program that calculates the area of a rectangle, 
# triangle and circle (write three functions to calculate the area. 
# And call them in the main program depending on the user's choice).

import math

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
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
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

while True:
    print("\nArea Calculator")
    print("1 - Rectangle\n2 - Triangle\n3 - Circle")
    
    user_choice = input("\nChoose action: ")
    
    match user_choice:
        case "1":
            try:
                a, b = map(float, input("Enter the sides of the rectangle (a, b): ").split())
                print(f"Result: {rectangle_area(a, b):.2f} cm²")
            except ValueError:
                print("Invalid input! Please enter two positive numbers.")
            break
        case "2":
            try:
                a, b, c = map(float, input("Enter the sides of the triangle (a, b, c): ").split())
                result = triangle_area(a, b, c)
                print(f"Result: {result:.2f} cm²" if isinstance(result, float) else result)
            except ValueError:
                print("Invalid input! Please enter three positive numbers.")
            break
        case "3":
            try:
                r = float(input("Enter the radius of the circle (r): "))
                if r > 0:
                    print(f"Result: {circle_area(r):.2f} cm²")
                else:
                    print("Radius must be positive.")
            except ValueError:
                print("Invalid input! Please enter a positive number.")
            break
        case _:
            print("Invalid choice! Please enter 1, 2, or 3.")

