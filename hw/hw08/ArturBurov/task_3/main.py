from shapes import rectangle_area, triangle_area, circle_area


def main():
    while True:
        print("\nChoose the figure to calculate the area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter the number of the figure (1-4): ")

        if choice == '1':
            a = float(input("Enter the length of side a: "))
            b = float(input("Enter the length of side b: "))
            print(f"The area of the rectangle is: {rectangle_area(a, b)}")

        elif choice == '2':
            base = float(input("Enter the base length: "))
            height = float(input("Enter the height: "))
            print(f"The area of the triangle is: {triangle_area(base, height)}")

        elif choice == '3':
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is: {circle_area(radius)}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
