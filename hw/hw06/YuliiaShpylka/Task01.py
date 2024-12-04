even = []
odd = []
not_divisible = []
for i in range(1, 10):
    if (i % 2) == 0 and (i % 3) == 0:
        even.append(i)
        odd.append(i)
    elif (i % 2) == 0:
        even.append(i)
    elif (i % 3) == 0:
        odd.append(i)
    else:
        not_divisible.append(i)
n = '\n'
print(f" Even numbers:{even}, {n} Odd numbers:{odd}, {n} Not divisible numbers: {not_divisible}")

