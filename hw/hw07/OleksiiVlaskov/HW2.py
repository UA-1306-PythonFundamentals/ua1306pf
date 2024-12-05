print("""Write a program that calculates the area of ​a rectangle, triangle and circle
(write three functions to calculate the area, and call them in the  
main program depending on the user's choice)""")

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
    PI = 3.14159265359
    result = round(PI * radius**2, 2)
    return result

user_input=input("""This program can calculate the area of a rectangle, triangle and circle
if you want to calculate:
rectangle - enter 1;
triangle - enter 2;
circle - enter 3;

Your choice: """)

if not user_input.isdigit() or int(user_input) > 3:
    raise Exception('Enter number 1, 2 or 3')

match (user_input):
    case '1':
        try:
            length, width = input("Enter length and width of the rectangle:\n").split()
            print(f"Area of the rectangle is: {area_rectangle(length=float(length),width=float(width))}")
        except:
            print(f"lenght or width is not a number")
    case '2':
        try:
            base, p_height = input("Enter base and perpendicular height of the triangle:\n").split()
            print(f"Area of the triangle is: {area_triangle(base=float(base),p_height=float(p_height))}")
        except:
            print(f"base or perpendicular height is not a number")
    case '3':
        try:
            radius = input("Enter radius of the circle:\n")
            print(f"Area of the circle is: {area_circle(radius=float(radius))}")
        except:
            print(f"radius is not a number")