# Task3: Write a script that will calculate the factorial of the entered 
# number without using recursion.
# Example: 0! = 1, 1! = 1, 2! = 2, 3! = 1 * 2 * 3 = 6, ….

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")
