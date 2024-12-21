import math


# Module with area calculation functions
def rectangle_area(a, b):
    """Calculate the area of a rectangle with sides a and b."""
    return a * b


def triangle_area(base, height):
    """Calculate the area of a triangle with base and height."""
    return 0.5 * base * height


def circle_area(radius):
    """Calculate the area of a circle with radius."""
    return math.pi * math.pow(radius, 2)


# Main module
if __name__ == "__main__":
    while True:
        print("\nChoose the shape to calculate the area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                a = float(input("Enter the length of side a: "))
                b = float(input("Enter the length of side b: "))
                area = rectangle_area(a, b)
                print(f"The area of the rectangle is {area}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '2':
            try:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = triangle_area(base, height)
                print(f"The area of the triangle is {area}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '3':
            try:
                radius = float(input("Enter the radius of the circle: "))
                area = circle_area(radius)
                print(f"The area of the circle is {area}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")
