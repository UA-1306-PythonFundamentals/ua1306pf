even_division_2 = [num for num in range(1, 11) if num % 2 == 0]
odd_division_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 == 0]
not_division_2_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]

print("Ділиться на 2:", even_division_2)
print("Ділиться на 3:", odd_division_3)
print("Не ділиться на 2 і 3:", not_division_2_3)
