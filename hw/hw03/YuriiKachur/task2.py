# Задаємо чотиризначне число
number = 9537

# Знаходимо добуток цифр
product = 1
for digit in str(number):
    product *= int(digit)

# Цифри у зворотньому порядку
reversed_number = int(str(number)[::-1])

# Цифри у зростаючому порядку
sorted_digits = int("".join(sorted(str(number))))

# Вихід
print(f"Product of digits: {product}")
print(f"Reversed number: {reversed_number}")
print(f"Digits in ascending order: {sorted_digits}")
