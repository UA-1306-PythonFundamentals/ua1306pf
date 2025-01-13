def day_of_week(number):
    """Returns the day of the week for a given number."""
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    try:
        number = int(number)
        if 1 <= number <= 7:
            return f"{number} corresponds to {week[number - 1]}"
        return "The number must be between 1 and 7."
    except ValueError:
        return "Invalid input. Please enter a valid number."


# Get user input and print the result
number = input("Enter a number between 1 and 7: ")
print(day_of_week(number))
