def largest_number(num1, num2):
    """This function determines the largest number between 2 inputs"""
    
    if num1 > num2:
        return num1
    elif num1 == num2:
        x = "Entered numbers are equal"
        return x
    else:
        return num2



print(largest_number(3, 9))


