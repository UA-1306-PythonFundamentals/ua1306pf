import random


def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Set the maximum number of attempts
    attempts = 10

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    # Loop for the number of attempts
    for attempt in range(1, attempts + 1):
        # Ask the user to guess a number
        guess = int(input(f"Attempt {attempt}/{attempts}. Enter your guess: "))

        # Check if the guessed number is correct
        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the correct number {number_to_guess}!")
            break
        elif guess < number_to_guess:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

    # If the user didn't guess the number in 10 attempts
    if guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")


# Run the game
guess_the_number()
