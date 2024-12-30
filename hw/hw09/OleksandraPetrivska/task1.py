import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guess the Number")

clock = pygame.time.Clock()


lower_bound = 1
upper_bound = 100
max_attempts = 10


secret_number = random.randint(lower_bound, upper_bound)


font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 48)


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

def check_guess(guess, secret_number):
    """Check if the guess is too low, too high, or correct."""
    if guess == secret_number:
        return "Correct", GREEN
    elif guess < secret_number:
        return "Too low", BLUE
    else:
        return "Too high", RED

def draw_text(text, x, y, font, color=WHITE):
    """Helper function to draw text on the screen."""
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def draw_gradient_background():
    """Draw a colorful gradient background."""
    for i in range(screen_height):
        color = (
            int((i / screen_height) * 255),  
            int((1 - i / screen_height) * 255),  
            int((i / screen_height) * 128)  
        )
        pygame.draw.line(screen, color, (0, i), (screen_width, i))

def play_game():
    attempts = 0
    guess = ""
    message = "Guess a number between {} and {}".format(lower_bound, upper_bound)
    game_over = False
    won = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    if guess != "":
                        attempts += 1
                        result, color = check_guess(int(guess), secret_number)

                        if result == "Correct":
                            message = f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts."
                            won = True
                            game_over = True
                        else:
                            message = f"{result}. Try again!"
                        guess = "" 
                    else:
                        message = "Please enter a number."

                elif event.key == pygame.K_BACKSPACE: 
                    guess = guess[:-1]

                elif event.key in range(pygame.K_0, pygame.K_9 + 1): 
                    guess += chr(event.key)

     
        draw_gradient_background()

        
        draw_text(message, 20, 20, font)

        text_color = WHITE
        if attempts > 0 and not won:
            result, text_color = check_guess(int(guess) if guess else 0, secret_number)
        draw_text("Attempts: {}/{}".format(attempts, max_attempts), 20, 60, font)
        draw_text("Your guess: " + guess, 20, 100, input_font)

        if attempts == max_attempts and not won:
            message = f"Game Over! The secret number was {secret_number}. Press the close button to exit."

        if won:
            draw_text("Press the close button to exit", 20, 140, font)

        
        pygame.display.flip()

        
        clock.tick(60)

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()

    