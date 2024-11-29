num = input("Please enter number: ")
convert_int_num = int(num)
factorial_result = 1
for i in range(1, convert_int_num + 1):
  if len(range(convert_int_num)) <= 1:
    break
  factorial_result *= i
print(f"{convert_int_num}! = {factorial_result}")