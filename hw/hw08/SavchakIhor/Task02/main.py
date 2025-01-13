from pasw_validation import password_validation


def main():
    user_input = input("Please enter password: ")
    print(password_validation(user_input))


if __name__ == '__main__':
    main()
