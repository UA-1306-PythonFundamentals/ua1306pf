from random import randint

count = 1
while count <= 10:
    rand_number = randint(1, 100)
    user_input = int(input("Please enter numer: "))
    user_unswer = input("Enter greater or less to gess number: ")
    count += 1
    if user_input > rand_number:
        x = True
    else:
        x  = False

    if user_unswer == "greater" and (x is True):
        print("Your the guess number is greater, you won!")
        break
    elif user_unswer == "greater" and (x is False):
        continue
    elif user_unswer == "less" and (x is True):
        continue
    elif user_unswer == "less" and (x is False):
        print("Your the guess number is less, you won")
    else:
        continue





