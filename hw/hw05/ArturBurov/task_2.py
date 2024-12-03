def print_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b


fibo = int(input("Enter a number: "))  # 21 -> 0 1 1 2 3 5 8 13 21
print_fibonacci(fibo)
