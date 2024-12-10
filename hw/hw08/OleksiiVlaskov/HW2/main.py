from validation import regex_validation
def main():
    print('''Write down your password below with these requirements in mind:
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters:
    
    ''')
    input_password=input('Password: ')
    print(regex_validation(input_string=input_password))
    

if __name__ == '__main__':
    main()