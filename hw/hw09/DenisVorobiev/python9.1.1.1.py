import random


secret_number = random.randint(1, 100)
attempts = 4

print("select number 1 - 100: ")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: "))

    if guess == secret_number:
        print(f"You guessed it {secret_number} in {attempt} tries")
        break
    else:
        print("Didn't guess right!")
else:
    print(f"You have entered the wrong number, the number was {secret_number}.")
