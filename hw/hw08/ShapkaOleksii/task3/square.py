from geometry import rectangle, circle, triangle

print("Choose a shape to calculate the area:")
print("1: Rectangle")
print("2: Triangle")
print("3: Circle")

task = input("Enter your choice (1, 2, or 3): ")

if task == "1":
    a = float(input("Enter length (a): "))
    b = float(input("Enter width (b): "))
    print(f"Area of rectangle = {rectangle(a, b):.2f}")
elif task == "2":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print(f"Area of triangle = {triangle(base, height):.2f}")
elif task == "3":
    r = float(input("Enter radius: "))
    print(f"Area of circle = {circle(r):.2f}")
else:
    print("Wrong choice, try again!")