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
    # PI = 3,14
    area = (r**2) * 3.14
    return area

user_input = input("""Please choose function for calculation:
1 - rectangle, 2 - triangle, 3 - circle: """)

if int(user_input) == 1:
    lenght = input("Please eneter Lenght: ")
    width = input("Please enetr Width: ")
    print(area_rectangle(int(lenght), int(width)))
elif int(user_input) == 2:
    base = input("Please eneter Base: ")
    hight = input("Please enter Hight: ")
    print(area_triangle(int(base), int(hight)))
else:
    radius = input("Please eneter Radius: ")
    print(area_circle(int(radius)))

