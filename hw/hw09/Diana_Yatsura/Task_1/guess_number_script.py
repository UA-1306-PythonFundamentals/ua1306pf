import random
from random import randint

random_n = (randint (1, 100 ))

def number_guessing():
    print('Welcome to the Guessing Game\n'
          'Try to guess the number between 1 and 100 but you are limited by 10 attempts')
    attempts = 0

    while attempts < 10:
        try:
            n = int(input(f'Attempt number {attempts + 1}/10: enter a number  between 1 and 100 '))
            if n < 1 or n > 100:
                print("Please, enter a number  between 1 and 100 ")
                continue
            elif n == random_n:
                print('WOW! You\'ve done amazing job')
                break
            elif n < random_n:
                dif = (random_n - n)/10
                print(f"Try again. You need to add {dif} tens. ")
            elif n > random_n:
                dif_1 = (n - random_n)/10
                print(f"Try again. You need to remove {dif_1} tens. ")
            attempts += 1
        except ValueError:
            print('invalid input. Please, enter an integer')

        if attempts == 10 and n != random_n:
            print(f'Sorry, you\'ve already used 10 attempts.\n'
                  f'The correct number is {random_n}')

number_guessing()