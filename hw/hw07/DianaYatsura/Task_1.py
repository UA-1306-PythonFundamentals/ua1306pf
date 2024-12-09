def largest_number ():
    """This function returns the largest number of two
numbers"""
    list_input = input("Enter two numbers: ").split(" ")
    num = list(map(int, list_input))
    return  max(num)


print(f"The largest number is: {largest_number()}")
print(largest_number.__doc__)