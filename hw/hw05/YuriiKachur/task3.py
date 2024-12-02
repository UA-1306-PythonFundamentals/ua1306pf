# Task 3
num = int(input("Введіть число для обчислення факторіала: "))

# розрахунок факторіалу за допомогою циклу
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"Факторіал {num} є: {factorial}")
