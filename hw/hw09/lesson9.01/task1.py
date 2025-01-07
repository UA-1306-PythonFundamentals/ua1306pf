import pygame
import random
import sys


pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вгадай число")

# Налаштування шрифтів і кольорів
FONT = pygame.font.Font(None, 36)
BIG_FONT = pygame.font.Font(None, 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Загадане число
target_number = random.randint(1, 100)
attempts_left = 10
message = "Введіть число від 1 до 100:"
input_text = ""

def draw_text(text, font, color, x, y):
    """Функція для відображення тексту на екрані."""
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def reset_game():
    """Функція для перезапуску гри."""
    global target_number, attempts_left, message, input_text
    target_number = random.randint(1, 100)
    attempts_left = 10
    message = "Введіть число від 1 до 100:"
    input_text = ""

# Основний ігровий цикл
running = True
while running:
    screen.fill(WHITE)
    
    # Відображення текстів
    draw_text("Гра: Вгадай число", BIG_FONT, BLACK, 150, 20)
    draw_text(f"Спроб залишилось: {attempts_left}", FONT, BLACK, 20, 80)
    draw_text(message, FONT, BLACK, 20, 140)
    draw_text(input_text, FONT, GREEN, 20, 180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # Обробка введення тексту
            if event.key == pygame.K_RETURN:  # Користувач натиснув Enter
                try:
                    user_guess = int(input_text)
                    if user_guess == target_number:
                        message = f"Вітаю! Ви вгадали число {target_number}!"
                        attempts_left = 0
                    elif user_guess < target_number:
                        message = "Число більше."
                    else:
                        message = "Число менше."
                    
                    attempts_left -= 1
                    input_text = ""
                    
                    if attempts_left == 0 and message != f"Вітаю! Ви вгадали число {target_number}!":
                        message = f"Ви програли. Загадане число: {target_number}."
                except ValueError:
                    message = "Будь ласка, введіть коректне число."
                    input_text = ""
            
            elif event.key == pygame.K_BACKSPACE:  # Видалення символу
                input_text = input_text[:-1]
            elif event.key == pygame.K_r:  # Перезапуск гри
                reset_game()
            else:  # Введення символів
                input_text += event.unicode

    # Якщо гра завершена, показуємо інструкцію для перезапуску
    if attempts_left == 0:
        draw_text("Натисніть 'R' для перезапуску гри", FONT, RED, 20, 220)

    # Оновлення екрана
    pygame.display.flip()

# Завершення роботи pygame
pygame.quit()
sys.exit()
