even, odd, not_divisible = [], [], []

for num in range(1, 10):
    if num % 2 == 0:
        print(f'{num} is an even number')
        even.append(num)
    elif num % 3 == 0:
        print(f'{num} is an odd number')
        odd.append(num)
    else:
        print(f'{num} is not divisible by 2 or 3')
        not_divisible.append(num)

print('Even numbers:', even)
print('Odd numbers:', odd)
print('Numbers not divisible by 2 or 3:', not_divisible)
