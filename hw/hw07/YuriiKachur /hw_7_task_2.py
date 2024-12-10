import math


def area_of_rectangle(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float or int): The length of the rectangle.
    width (float or int): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width


def area_of_triangle(base, height):
    """
    Calculates the area of a triangle.

    Parameters:
    base (float or int): The base of the triangle.
    height (float or int): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height


def area_of_circle(radius):
    """
    Calculates the area of a circle.

    Parameters:
    radius (float or int): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2


def main():
    """
    Main function that allows the user to select a shape
    and calculates its area.
    """
    print("Виберіть фігуру, щоб обчислити її площу:")
    print("a. Прямокутник")
    print("b. Трикутник")
    print("c. Коло")

    # Цикл для перевірки правильного вибору
    choice = input("Зробіть Ваш вибір (a/b/c): ")
    while choice not in ['a', 'b', 'c']:
        print("Невірний вибір! Будь ласка, введіть a, b або c.")
        choice = input("Зробіть Ваш вибір (a/b/c): ")

    # Виконання обчислень залежно від вибору
    if choice == 'a':
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        print(f"Площа прямокутника: {area_of_rectangle(length, width)}")
    elif choice == 'b':
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        print(f"Площа трикутника: {area_of_triangle(base, height)}")
    elif choice == 'c':
        radius = float(input("Введіть радіус кола: "))
        print(f"Площа кола: {area_of_circle(radius)}")


# Run the main program
if __name__ == "__main__":
    main()
