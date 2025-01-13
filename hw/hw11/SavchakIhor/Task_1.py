class AgeError(Exception):
    """Custom exception for invalid age input."""
    def __init__(self, message='Age cannot be zero or negative'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


def validate_age_input(age_input):
    """Validates the age input."""
    try:
        age = float(age_input)
        if age <= 0:
            raise AgeError(f'Invalid input: {age_input}. Age must be a positive number.')
        return age
    except ValueError:
        raise ValueError("You entered an invalid value. Please enter a numeric value.")


def check_odd_or_even(age):
    """Checks if the age is odd or even."""
    if age % 2 == 0:
        return f"Your age {age} is even."
    else:
        return f"Your age {age} is odd."


def process_age_input(age_input):
    """Processes the age input and checks if it is valid, then checks odd or even."""
    try:
        age = validate_age_input(age_input)
        return check_odd_or_even(age)
    except (ValueError, AgeError) as error:
        return str(error)


# Get user input
age_input = input("Enter your age: ")
print(process_age_input(age_input))
