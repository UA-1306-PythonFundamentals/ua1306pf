import pygame
import sys


pygame.init()

# Розміри вікна
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rectangle Movement")

# Властивості прямокутника
rect_width = 50
rect_height = 50
rect_x = 100  # Початкова координата X
rect_y = 100  # Початкова координата Y
rect_speed_x = 5
rect_speed_y = 5

# Основний цикл програми
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Оновлення позиції прямокутника
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Перевірка меж, щоб прямокутник не виходив за вікно
    if rect_x < 0:
        rect_x = 0
        rect_speed_x *= -1
    if rect_x + rect_width > window_width:
        rect_x = window_width - rect_width
        rect_speed_x *= -1
    if rect_y < 0:
        rect_y = 0
        rect_speed_y *= -1
    if rect_y + rect_height > window_height:
        rect_y = window_height - rect_height
        rect_speed_y *= -1

    # Очищення вікна
    window.fill((0, 0, 0))

    # Малювання прямокутника
    pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

    # Оновлення екрану
    pygame.display.flip()

    # Затримка
    pygame.time.delay(30)
