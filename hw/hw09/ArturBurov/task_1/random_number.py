import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Guess the secret number")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

font = pygame.font.Font(None, 36)

secret_number = random.randint(1, 100)
attempts_left = 10
user_input = ""
message = ""
game_over = False


def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif not game_over:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(user_input)
                        attempts_left -= 1

                        if guess == secret_number:
                            message = f"Congratulations! You guessed the number {secret_number}"
                            game_over = True
                        elif guess < secret_number:
                            message = "Too low!"
                        else:
                            message = "Too high!"

                        if attempts_left == 0 and guess != secret_number:
                            message = f"You ran out of attempts! The number was {secret_number}"
                            game_over = True
                    except ValueError:
                        message = "Invalid input. Please enter a number."

                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isdigit():
                    user_input += event.unicode
            else:
                if event.key == pygame.K_RETURN:
                    secret_number = random.randint(1, 100)
                    attempts_left = 10
                    user_input = ""
                    game_over = False
                    message = ""

    screen.fill(white)

    display_text("Guess the number (1-100)", black, screen_width // 2, 50)
    display_text(f"Attempts left: {attempts_left}", black, screen_width // 2, 100)
    display_text(f"Your guess: {user_input}", black, screen_width // 2, 150)
    display_text(message, green if "Congratulations" in message else red, screen_width // 2, 250)

    if game_over:
        display_text("Press Enter to play again or Q to quit", black, screen_width // 2, 350)
    else:
        display_text("Press Q to quit", black, screen_width // 2, 350)

    pygame.display.flip()

pygame.quit()
