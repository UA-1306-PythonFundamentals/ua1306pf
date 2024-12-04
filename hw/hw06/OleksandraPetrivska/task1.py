not_div_2_3 = [n for n in range(1, 11) if n % 2 != 0 and n % 3 != 0]
even_num_div_2 = [n for n in range(1, 11) if n % 2 == 0]
odd_num_div_3 = [n for n in range(1, 11) if n % 2 != 0 and n % 3 == 0]

print("Numbers not divisible by 2 and 3:", not_div_2_3)
print("Even numbers divisible by 2:", even_num_div_2)
print("Odd numbers divisible by 3:", odd_num_div_3)

