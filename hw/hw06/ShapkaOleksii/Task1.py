
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = []
oddNumbers = []
notDivis = []

evenNumbers = [i for i in numbers if i % 2 == 0]
oddNumbers = [i for i in numbers if i % 2 != 0 and i % 3 == 0]
notDivis = [i for i in numbers if i % 2 != 0 and i % 3 != 0 ]

print(f"Even numbers (divisible by 2): {evenNumbers}")
print(f"Odd numbers (divisible by 3): {oddNumbers}")
print(f"Numbers not divisible by 2 or 3: {notDivis}")