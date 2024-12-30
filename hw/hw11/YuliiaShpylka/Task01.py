class MyError(Exception):
    def __init__(self):
        self.message = "Incorrect value. Entered age is less or equal to 0"

def even_odd_age(age):
    try:
        if int(age) <= 0:
            raise MyError()
        if int(age) % 2 == 0:
            return(f"Your age {age} is even number")
        else:
            return(f"Your age {age} is odd number")
    except ValueError:
        return(f"This is not number. Please enter number")
    except MyError as e:
        return(e.message)


def main():
    user_input = input("Please enter your age: ")
    result = even_odd_age(user_input)
    print(result)


if __name__ == '__main__':
    main()

