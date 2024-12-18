def find_largest(num1, num2):
    """Returns the larger of two numbers.

    Args:
      num1: The first number.
      num2: The second number.

    Returns:
      The larger of the two numbers. Returns num1 if the numbers are equal.
    """
    if num1 >= num2:
        return num1
    else:
        return num2


print(find_largest(7, 15))  # Output: 15
