def fibonacci_numbers(n):
    i = 0
    j = 1
    while i <= n:
        print(i, end=' ')
        i, j = j, i + j


fibonacci_numbers(int(input('Enter a number ')))