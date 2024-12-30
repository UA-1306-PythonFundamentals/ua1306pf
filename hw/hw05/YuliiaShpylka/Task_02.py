number = input("Please enter number: ")
num1 = 0
num2 = 1
next_number = num2
k = 1
l = ["0", "1"]
while k <= int(number):
    # print(next_number, end=" ")
    l.append(str(next_number))
    k += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
fibonacci_str = " ".join(l)
print(fibonacci_str)