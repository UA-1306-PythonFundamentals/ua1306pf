def rectangle_area(a, b):
    s = a * b
    return s

def circle_area(a):
    s = a ** 2 * 3.14
    return s

def triangle_area(a, b):
    s = a * b * 1 / 2
    return s

selector = int(input("""
                     Enter 1 for rectangle, 
                     2 for triangle, 
                     3 for circle: """))
if selector == 1:
    a = int(input("enter rectangle height: "))
    b = int(input("enter rectangle width: "))
    print(f"The area of your rectangle is: {rectangle_area(a, b)}")
elif selector == 2:
    a = int(input("enter triangle height: "))
    b = int(input("enter triangle width: "))
    print(f"The area of your triangle is: {triangle_area(a, b)}")
elif selector == 3:
    a = int(input("enter circle radius: "))
    print(f"The area of your circle is: {circle_area(a)}")
else:
    print("enter numbers 1 - 3")