number = input("Enter a four-digit number: ")

digits = []

for d in number:
    digits.append(int(d))
    
    product = 1
    for digit in digits:
        product *= digit
    print(f"Product of the digits: {product}")

    # 2. Write the number in reverse order
    reversed_number = number[::-1]
    print(f"Reversed number: {reversed_number}")

    # 3. Sort the digits in ascending order
    sorted_digits = ''.join(sorted(number))
    print(f"Digits in ascending order: {sorted_digits}")
else:
    print("Please enter a valid four-digit natural number.")