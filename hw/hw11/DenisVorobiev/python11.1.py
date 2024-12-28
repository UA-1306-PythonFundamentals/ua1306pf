def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2 == 0:
        return "/2 "
    else:
        return "not /2 "

try:
    age = int(input("Enter your age: "))
    print(process_age(age))
except ValueError as e:
    print(f"Error: {e}")