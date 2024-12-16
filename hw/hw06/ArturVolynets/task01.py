# Task 1: In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

numbers = list(range(1, 11))
print(f"Numbers list: {numbers}")

even_numbers = [number for number in numbers if number % 2 == 0]
print(f"Even numbers list: {even_numbers}")

odd_numbers = [number for number in numbers if number % 3 == 0]
print(f"Odd numbers list: {odd_numbers}")

not_divisible_numbers = [number for number in numbers if not (number % 2 == 0 or number % 3 == 0)]
print(f"Not divisible numbers list: {not_divisible_numbers}")
