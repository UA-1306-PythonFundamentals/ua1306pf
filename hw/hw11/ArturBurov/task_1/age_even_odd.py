class NegativeAgeException(Exception):
    """Custom exception raised for negative age input."""
    def __init__(self, message="Age cannot be negative."):
        self.message = message
        super().__init__(self.message)


def check_age_even_odd(age):
    if age < 0:
        raise NegativeAgeException()  # Raise the exception with the default message
    elif age % 2 == 0:
        return "The age is even."
    else:
        return "The age is odd."


def main():
    try:
        age = int(input("Enter your age: "))
        result = check_age_even_odd(age)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")
    except NegativeAgeException as e:
        print(e)  # Print the message associated with the exception


if __name__ == "__main__":
    main()