def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i  # 0!=1, 1!=1, 2!=1*2, 3!=1*2*3=6, 4!=1*2*3*4=24, 5!=1*2*3*4*5=120
    return result


number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")  # 5 -> The factorial of 5 is: 120
