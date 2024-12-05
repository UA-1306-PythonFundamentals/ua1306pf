import math


def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle.

    Args:
      length: The length of the rectangle.
      width: The width of the rectangle.

    Returns:
      The area of the rectangle, rounded to two decimal places.
    """
    return round(length * width, 2)


def calculate_triangle_area(base, height):
    """Calculates the area of a triangle.

    Args:
      base: The base of the triangle.
      height: The height of the triangle.

    Returns:
      The area of the triangle, rounded to two decimal places.
    """
    return round(0.5 * base * height, 2)


def calculate_circle_area(radius):
    """Calculates the area of a circle.

    Args:
      radius: The radius of the circle.

    Returns:
      The area of the circle, rounded to two decimal places.
    """
    return round(math.pi * radius ** 2, 2)


def main():
    """Main function to interact with the user and calculate areas."""
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print("The area of the rectangle is:", area)
    elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print("The area of the triangle is:", area)
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print("The area of the circle is:", area)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
