def largest_number(a, b):
    """
    This function compares two numbers
    and returns the largest number of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: the largest number.
    """
    if a > b:
        return a
    if b > a:
        return b
print(largest_number(4,302))
print(largest_number(432,0))
print(largest_number(-4,0))

