def even_odd(num):
    if num % 2 == 0:
        return 'even'
    return 'odd'


if __name__ == "__main__":
    user_age = int(input('Enter your age: '))
    if user_age >= 0:
        print(even_odd(user_age))
    else:
        raise ValueError('Negative numbers not allowed')
