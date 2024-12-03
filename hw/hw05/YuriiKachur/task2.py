# Task 2
n = int(input("Введіть число для створення послідовності Фібоначчі: "))

# Ініціалізація перші два числа в послідовності
a, b = 0, 1
fibonacci_progression = []

# Генерація номерів Фібоначчі
while a <= n:
    fibonacci_progression.append(a)
    a, b = b, a + b

print("Послідовність Фібоначчі", n, ":", fibonacci_progression)
