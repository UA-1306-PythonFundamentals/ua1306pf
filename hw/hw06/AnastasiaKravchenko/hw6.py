# TODO: Task 1. In the range from 1 to 10 determine:
# - even numbers (div by 2)
# - odd numbers (div by 3)
# - other
def classify_numbers():
    result = {
        'even': [],
        'odd': [],
        'other': []
    }
    for i in range(1, 10):
        if i % 2 == 0:
            result['even'].append(i)
        elif i % 3 == 0:
            result['odd'].append(i)
        else:
            result['other'].append(i)
    return result


# print(classify_numbers())


# TODO: Task 2. Check user login. If "First" then greet user, otherwise - error. Use while loop.
user_login = input('Enter user login:\n')
while user_login != 'First':
    print('Error. Wrong login. Please try again.')
    user_login = input('Enter user login:\n')

print('Success! Nice to see you again!')
