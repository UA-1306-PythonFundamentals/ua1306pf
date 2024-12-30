import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

def main():
    print("Choose a shape to calculate its area:")
    print("1. Rectangle\n2. Triangle\n3. Circle")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(f"Area of rectangle: {area_rectangle(l, w):.2f}")
    elif choice == "2":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area of triangle: {area_triangle(b, h):.2f}")
    elif choice == "3":
        r = float(input("Enter radius: "))
        print(f"Area of circle: {area_circle(r):.2f}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()