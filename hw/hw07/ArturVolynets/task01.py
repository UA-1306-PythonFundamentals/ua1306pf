# Task1. Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def largest_number(a, b):
    """
    Return the largest of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The larger of the two input numbers.
    """
    return a if a > b else b

print(largest_number(17, 23))
print(largest_number(-34.123, 123.11111))
