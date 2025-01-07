# 2. Write a program that analyzes the entered number and, depending on the number, 
# gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
# Take into account cases of entering numbers from 8 and more, as well as cases 
# of entering non-numerical data.

class WrongDayError(Exception):
    """Exception for handling invalid day input."""
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return f"Invalid day: {self.day}. Please enter a number between 1 and 7."

week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

try:
    input_value = input("Enter your day of the week (1, 2, 3, ...): ")

    if not input_value.isdigit():
        raise ValueError(f"Invalid input: '{input_value}' is not a number.")

    day = int(input_value)

    if day not in range(1, 8):
        raise WrongDayError(day)

    print(f"{day} is {week[day]}")

except WrongDayError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

