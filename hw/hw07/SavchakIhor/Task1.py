def largest_number():
    """Returns the largest number among two input numbers."""
    num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())
    return max(num1, num2)

print(f"The largest number is: {largest_number()}")
print(largest_number.__doc__)