def largest_of_two_numbers(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float or int: The larger of the two input numbers.
    """
    return a if a > b else b

# Example usage
print("Largest of a and b is:", largest_of_two_numbers(10.3, 10.7))
print("Largest of a and b is:", largest_of_two_numbers(-3, 10))
print("Largest of a and b is:", largest_of_two_numbers(-100, -300))
