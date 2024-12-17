import pygame
import random


FPS = 60
WIDTH_DISPLAY = 600
HEIGHT_DISPLAY = 600
BLUE_COLOR = (51, 51, 255)
WHITE_COLOR = (255, 255, 255)
LIGHT_BLUE_COLOR = (153, 204, 255)
RED_COLOR = (255, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("Guess the Number")
clock = pygame.time.Clock()

random_n = random.randint(1, 100)
input_text = ""
feedback_text = "Please, enter a number between 1 and 100!"
attempts_list = []
max_attempts = 10
game_over = False

font_large = pygame.font.Font(None, 35)
font_small = pygame.font.Font(None, 25)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    user_n = int(input_text)
                    attempts_list.append(user_n)

                    if user_n == random_n:
                        feedback_text = f"WOW! WIN! The number was {random_n}."
                        game_over = True
                    elif len(attempts_list) >= max_attempts:
                        feedback_text = f"Game Over! The number was {random_n}."
                        game_over = True
                    elif user_n < random_n:
                        feedback_text = "Too low! Try a higher number."
                    elif user_n > random_n:
                        feedback_text = "Too high! Try a lower number."
                else:
                    feedback_text = "Invalid input! Enter a number."
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    gameDisplay.fill(BLUE_COLOR)

    feedback_surface = font_large.render(feedback_text, True, WHITE_COLOR)
    gameDisplay.blit(feedback_surface, (WIDTH_DISPLAY // 2 - feedback_surface.get_width() // 2, 30))
    pygame.draw.circle(gameDisplay,LIGHT_BLUE_COLOR, (WIDTH_DISPLAY // 2, HEIGHT_DISPLAY // 2 - 50), 50)
    if game_over:
        pygame.draw.circle(gameDisplay, RED_COLOR, (WIDTH_DISPLAY // 2, HEIGHT_DISPLAY // 2 - 50), 50)
        result_surface = font_large.render(str(random_n), True, WHITE_COLOR)
        gameDisplay.blit(result_surface, result_surface.get_rect(center=(WIDTH_DISPLAY // 2, HEIGHT_DISPLAY // 2 - 50)))

    if input_text.isdigit():
        guess_surface = font_small.render(input_text, True, WHITE_COLOR)
        gameDisplay.blit(guess_surface, guess_surface.get_rect(center=(WIDTH_DISPLAY // 2, HEIGHT_DISPLAY // 2 - 50)))

    rectangle_y_position = HEIGHT_DISPLAY // 2 + 50
    pygame.draw.rect(gameDisplay, LIGHT_BLUE_COLOR, (50, rectangle_y_position, WIDTH_DISPLAY - 100, 100), 0)
    attempts_text = ", ".join(map(str, attempts_list))
    attempts_surface = font_small.render("Attempts: " + attempts_text, True, WHITE_COLOR)
    gameDisplay.blit(attempts_surface, (60, rectangle_y_position + 40))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()