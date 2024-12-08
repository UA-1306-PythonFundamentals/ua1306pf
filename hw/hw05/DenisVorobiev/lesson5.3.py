n = int(input("input number: "))
if n < 0:
    print("not support - ")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial {n} is {result}")
