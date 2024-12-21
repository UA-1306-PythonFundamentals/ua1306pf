import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

RECT_WIDTH = 40
RECT_HEIGHT = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")
rect = pygame.Rect(50, 50, RECT_WIDTH, RECT_HEIGHT)

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        rect.x -= DELTA_STEP
    if keys[pygame.K_RIGHT]:
        rect.x += DELTA_STEP
    if keys[pygame.K_UP]:
        rect.y -= DELTA_STEP
    if keys[pygame.K_DOWN]:
        rect.y += DELTA_STEP


    rect.clamp_ip(gameDisplay.get_rect())


    gameDisplay.fill(BLACK_COLOR)
    pygame.draw.rect(gameDisplay, RED_COLOR, rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
    

