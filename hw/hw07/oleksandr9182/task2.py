def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return 3.14159 * radius ** 2


choice = input("Choose a shape (rectangle/triangle/circle): ").lower()

if choice == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print(f"The area of the rectangle is: {rectangle_area(length, width)}")
elif choice == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print(f"The area of the triangle is: {triangle_area(base, height)}")
elif choice == "circle":
    radius = float(input("Enter the radius: "))
    print(f"The area of the circle is: {circle_area(radius)}")
else:
    print("Invalid choice.")
