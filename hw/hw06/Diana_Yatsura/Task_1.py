even, odd, not_divisible = [], [], []
for num in range(1, 10):
    if num % 2 == 1 and num % 3 == 1:
        print(f'{num} is not divisible by 2 and 3')
        not_divisible.append(num)
    elif num % 2 == 0:
        print (f'{num} is even number')
        even.append(num)
    elif num % 3 == 0:
        print(f'{num} is odd number')
        odd.append(num)
print('Even numbers are =', even)
print ('Odd numbers are =', odd)
print('Numbers, that are not divisible by 2 and 3 =', not_divisible)
