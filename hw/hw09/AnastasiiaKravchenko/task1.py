from random import randint


def guess_number(user_num):
    if user_num > random_num:
        return f'{user_num} is too high', False
    elif user_num < random_num:
        return f'{user_num} is too low', False
    return f'{user_num} is correct! Congrats!', True


random_num = randint(1, 100)
for _ in range(10):
    user_input = int(input('Guess the number from 1 to 100: '))
    msg, is_correct = guess_number(user_input)
    print(msg)
    if is_correct:
        break
else:
    print('Game over! You\'re out of tries')
