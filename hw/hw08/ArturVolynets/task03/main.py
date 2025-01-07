from area import *

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


