from calculations import rectangle_area, triangle_area, circle_area

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        if length > 0 and width > 0:
            area = rectangle_area(length, width)
            print("The area of the rectangle is:", area)
        else:
            print("Please enter positive values for length and width!")

    elif choice == "2":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        if base > 0 and height > 0:
            area = triangle_area(base, height)
            print("The area of the triangle is:", area)
        else:
            print("Please enter positive values for base and height!")

    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        if radius > 0:
            area = circle_area(radius)
            print("The area of the circle is:", round(area, 2))
        else:
            print("Please enter a positive value for the radius!")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

