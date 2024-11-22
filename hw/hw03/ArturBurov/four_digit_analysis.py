def analyze_number(number):
    if not 1000 <= number <= 9999:
        raise ValueError("Input must be a four-digit number.")

    num_str = str(number)

    # 1. Find the product of digits
    product = 1
    for digit in num_str:
        product = product * int(digit)

    # 2. Reverse the number
    reversed_num = int(num_str[::-1])

    # 3. Sort digits in ascending order
    digit_list = []
    for digit in num_str:
        int_digit = int(digit)
        digit_list.append(int_digit)

    sorted_digits = sorted(digit_list)

    print(f"Original number: {number}")
    print(f"Product of digits: {product}")
    print(f"Reversed number: {reversed_num}")
    print(f"Sorted digits: {sorted_digits}")


analyze_number(1134)
