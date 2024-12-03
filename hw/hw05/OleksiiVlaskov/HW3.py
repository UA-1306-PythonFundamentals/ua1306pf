print('''Task3. Write a script that will calculate the factorial of the entered 
number without using recursion.
Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, ….

''')

entered_number=input("Enter an integer n and this script will print the factorial of the entered number:\n")

check = int(entered_number) if entered_number.isdigit() or entered_number == "0" else None

if not check and check != 0:
    raise Exception("Please enter integer number")
  
factorial = 1
for a in range(1, check + 1):
    factorial *= a

print(f"{factorial=}")