import geometry

def main():
    print("Виберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Введіть номер обраної фігури (1/2/3): ")

    if choice == "1":
        a = float(input("Введіть довжину прямокутника (a): "))
        b = float(input("Введіть ширину прямокутника (b): "))
        print(f"Площа прямокутника: {geometry.rectangle_area(a, b)}")
    elif choice == "2":
        h = float(input("Введіть висоту трикутника (h): "))
        a = float(input("Введіть основу трикутника (a): "))
        print(f"Площа трикутника: {geometry.triangle_area(h, a)}")
    elif choice == "3":
        r = float(input("Введіть радіус кола (r): "))
        print(f"Площа кола: {geometry.circle_area(r)}")
    else:
        print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
