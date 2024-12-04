def factorial (num):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
num = int(input ('Enter a number '))
print (f'{num}! = {factorial(num)}')

# OR another version
for n in input("Enter a number "):
    print(f'{n}! = {math.factorial(int(n))}')