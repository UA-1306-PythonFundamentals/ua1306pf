def fibonacci_numbers(n):
    i = 0
    c = 1
    while i <= n:
        print(i, end=' ')
        i, c = c, i + c
fibonacci_numbers(int(input('Enter a number ')))