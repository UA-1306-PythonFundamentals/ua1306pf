from calc_area import area_rectangle, area_triangle, area_circle


def user_input():
    """
    Prompt the user to choose a shape and input the required dimensions
    for area calculation.
    """
    try:
        choice = int(input("""Please choose a function for calculation:
1 - Rectangle, 2 - Triangle, 3 - Circle: """))

        if choice == 1:
            length = float(input("Please enter Length: "))
            width = float(input("Please enter Width: "))
            print(f"The area of the rectangle is: {area_rectangle(length, width)}")

        elif choice == 2:
            base = float(input("Please enter Base: "))
            height = float(input("Please enter Height: "))
            print(f"The area of the triangle is: {area_triangle(base, height)}")

        elif choice == 3:
            radius = float(input("Please enter Radius: "))
            print(f"The area of the circle is: {area_circle(radius)}")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


def main():
    user_input()


if __name__ == '__main__':
    main()
