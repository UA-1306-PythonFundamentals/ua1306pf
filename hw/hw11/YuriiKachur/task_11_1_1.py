def age_input(age):
    if age < 0:
        raise ValueError("Невірно, вік не може бути відємним.")
    if age % 2 == 0:
        return "Твій вік парний"
    else:
        return "Твій вік непарний."

def main():
    while True:
        try:
            age = int(input("Введіть Ваш вік: "))
            message = age_input(age)
            print(message)
            break  # Вихід із циклу
        except ValueError as e:
            print(f"Error: {e}. Спробуйте ще.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Спробуйте ще.")

if __name__ == "__main__":
    main()
