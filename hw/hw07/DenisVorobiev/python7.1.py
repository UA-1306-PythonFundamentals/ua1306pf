def largest_number(a, b):
    """
    Returns the largest number.
    """
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Numbers not correct"

# Пример использования
num1 = float(input("first num: "))
num2 = float(input("second num: "))
result = largest_number(num1, num2)

print(f"The largest number is: {result}")