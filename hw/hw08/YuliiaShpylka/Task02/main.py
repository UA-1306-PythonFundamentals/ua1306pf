from pasw_validation import pasword_validation

def main():
    user_input = input("Please enter password: ")
    print(pasword_validation(user_input))

if __name__ == '__main__':
    main()