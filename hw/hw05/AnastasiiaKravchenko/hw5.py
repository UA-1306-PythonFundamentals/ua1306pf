# TODO: Change list elements' type to float

l = [11, 22, 33, 44, 55]
for elem in l:
    new_elem = float(elem)
    l[l.index(elem)] = new_elem
print(l)

# TODO: Fibonacci numbers
num = int(input('Enter number to see Fibonacci sequence: '))
fibonacci_list = [0, 1]
fibo_number = 1
while fibo_number <= num:
    fibonacci_list.append(fibo_number)
    fibo_number = fibonacci_list[-1] + fibonacci_list[-2]

print(fibonacci_list)

# TODO: Factorial
num = int(input('Enter number to get factorial: '))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)

# Another solution
num2 = int(input('Enter number to get factorial: '))
f = 1
for n in range(1, num2+1):
    f *= n
print(f)
