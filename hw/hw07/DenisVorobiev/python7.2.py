import math

def rectangle(length, width):
    return length * width

def triangle(base, height):
    return 0.5 * base * height

def circle(radius):
    return math.pi * radius ** 2

print("Оберіть фігуру:")
print("1. Ррямокутник")
print("2. Трикутник")
print("3. Коло")
choice = int(input("(1/2/3): "))

if choice == 1:
    length = float(input("Введіть довжину прямокутника: "))
    width = float(input("Введіть ширину прямокутника: "))
    print(f"Площа прямокутника: {rectangle(length, width)}")
elif choice == 2:
    base = float(input("Введіть основу трикутника: "))
    height = float(input("Введіть висоту трикутника: "))
    print(f"Площа трикутника: {triangle(base, height)}")
elif choice == 3:
    radius = float(input("Введіть радіус кола: "))
    print(f"Площа кола: {circle(radius)}")
else:
    print("Невірний вибір!")
