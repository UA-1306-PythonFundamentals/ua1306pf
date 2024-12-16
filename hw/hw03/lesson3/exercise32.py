def process_number(number):
    # Перевірка, що число чотиризначне
    if not (1000 <= number <= 9999):
        raise ValueError("Число має бути чотиризначним і натуральним.")

  
    digits = [int(d) for d in str(number)]   # Перетворення числа на список цифр

    # 1. Знайти добуток цифр
    product = 1
    for digit in digits:
        product *= digit

    # 2. Записати число у зворотньому порядку
    reversed_number = int(str(number)[::-1])

    # 3. Відсортувати цифри числа
    sorted_digits = ''.join(map(str, sorted(digits)))

    return product, reversed_number, sorted_digits


try:
    number = int(input("Введіть чотиризначне натуральне число: "))
    product, reversed_number, sorted_digits = process_number(number)

    print(f"Добуток цифр: {product}")
    print(f"Число у зворотньому порядку: {reversed_number}")
    print(f"Відсортовані цифри числа: {sorted_digits}")
except ValueError as e:
    print(e)
