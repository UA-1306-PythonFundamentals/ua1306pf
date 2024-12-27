class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative!")
    
    if age % 2 == 0:
        return f"Your age is {age}, which is even."
    else:
        return f"Your age is {age}, which is odd."

def get_age_from_user():
    while True:
        try:
            age = int(input("Please enter your age: "))
            
            result = check_age(age)
            
            print(result)
            break  
            
        except ValueError:
            print("Error: Please enter a valid number for age.")
        except AgeError as e:
            print(e)

get_age_from_user()

