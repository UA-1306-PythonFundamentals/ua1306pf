class Age_less_0(Exception):
    pass

def age_func(age):
    try:
        age=int(age)
        if age < 0:
            raise Age_less_0(f"{age} < 0")
        elif age % 2 == 0:
            print(f"Your age is even - {age=}")
        else:
            print(f"Your age is odd - {age=}")
    except ValueError:
        print("Enter number next time")
    except Age_less_0 as e:
        print("The entered number cannot be less than 0")
    
age=input("Enter your age:\n")
age_func(age)