import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Secret Number")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font
FONT = pygame.font.Font(None, 36)

# Game variables
secret_number = random.randint(1, 100)
attempts_left = 10
user_input = ""
message = ""
game_over = False

# Utility functions
def draw_text(text, color, center):
    rendered_text = FONT.render(text, True, color)
    text_rect = rendered_text.get_rect(center=center)
    screen.blit(rendered_text, text_rect)

def reset_game():
    global secret_number, attempts_left, user_input, message, game_over
    secret_number = random.randint(1, 100)
    attempts_left = 10
    user_input = ""
    message = ""
    game_over = False

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

            elif not game_over:
                if event.key == pygame.K_RETURN:
                    if user_input.isdigit():
                        guess = int(user_input)
                        attempts_left -= 1

                        if guess == secret_number:
                            message = f"Congratulations! You guessed it: {secret_number}"
                            game_over = True
                        elif guess < secret_number:
                            message = "Too low!"
                        else:
                            message = "Too high!"

                        if attempts_left == 0 and guess != secret_number:
                            message = f"Out of attempts! The number was {secret_number}"
                            game_over = True
                    else:
                        message = "Enter a valid number!"

                    user_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.unicode.isdigit():
                    user_input += event.unicode

            elif event.key == pygame.K_RETURN:
                reset_game()

    # Draw game elements
    draw_text("Guess the number (1-100)", BLACK, (WIDTH // 2, 50))
    draw_text(f"Attempts left: {attempts_left}", BLACK, (WIDTH // 2, 100))
    draw_text(f"Your guess: {user_input}", BLACK, (WIDTH // 2, 150))
    draw_text(message, GREEN if "Congratulations" in message else RED, (WIDTH // 2, 250))

    if game_over:
        draw_text("Press Enter to play again or Q to quit", BLACK, (WIDTH // 2, 350))
    else:
        draw_text("Press Q to quit", BLACK, (WIDTH // 2, 350))

    pygame.display.flip()

pygame.quit()
