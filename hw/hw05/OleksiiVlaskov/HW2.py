print('''Task2. Print Fibonacci numbers up to the entered number n, 
using cycles. 
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

''')

entered_number=input("Enter the number n and this script will print the Fibonacci number to your number:\n")

check = int(entered_number) if entered_number.isdigit() else None

if not check:
    raise Exception("Please enter integer number")

a,b = 0, 1

while a < check:
    print(a)
    a,b = b, a+b
    