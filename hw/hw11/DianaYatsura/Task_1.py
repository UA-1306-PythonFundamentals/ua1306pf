class MyError(Exception):
    def __init__(self, message = 'Negative number error'):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message


def check_age(age):
    try:
        if int(age) <= 0:
            raise MyError(f'Your input contain unappropriated number: {age}. Try again.')
        elif not isinstance(age, (str, int, float)):
            raise ValueError
        return check_odd_even(age)
    except ValueError:
        return "You entered not a number."
    except MyError as me:
        return me
age = input("Enter your age: ")


def check_odd_even(age):
    if int(age) % 2 == 0:
        return f"Your age {age} is even"
    elif int(age) % 2 == 1:
        return f"Your age {age} is odd"


print(check_age(age))