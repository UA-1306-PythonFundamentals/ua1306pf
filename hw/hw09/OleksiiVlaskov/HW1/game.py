import os
import pygame
from random import randint

NUMBER = randint(1,100)
FPS = 60
FORM_X, FORM_Y=600, 600

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "Play.jpg")
pygame.init()
form = pygame.display.set_mode((FORM_X, FORM_Y))
pygame.display.set_caption("You Wanna Play A Little Game?!")
background_image = pygame.image.load(image_path)
background_image = pygame.transform.scale(background_image, (FORM_X, FORM_Y))
run = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
text = """Guess the number I guessed. You have only 10 tries. 
I'll tell you if your number is less or more than the one I guessed. 
If you guess right, you get a prize, and if not, we'll see :)"""
input_rect = pygame.Rect(275, 470, 50, 25)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4') 
color = color_passive 
active = False
user_text = ''
end2 = False
gueses = 10
while run:
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos): 
                active = True
            else: 
                active = False
        
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                try:
                    if NUMBER == int(user_text):
                        text = 'Congratulations - You win'
                        end2=True
                        start1 = pygame.time.get_ticks()
                        end1 = start1 + 3000
                    elif NUMBER > int(user_text):
                        gueses -= 1
                        text = f'Wrong answer :)\nMy number: GREATER than yours\n{gueses} more attempts left'
                    elif NUMBER < int(user_text):
                        gueses -= 1
                        text = f'Wrong answer :)\nMy number: LESS than yours\n{gueses} more attempts left'
                except Exception as e:
                    text = f'ERROR: {e}'
            else:
                user_text += event.unicode
    if gueses == 0:
        text = 'You loose'
        start1 = pygame.time.get_ticks()
        end1 = start1 + 3000
        
    if active: 
        color = color_active 
    else: 
        color = color_passive
    
    form.blit(background_image, (0, 0))
    
    pygame.draw.rect(form, 'white', rect=[10, 500, 580, 90])
    pygame.draw.rect(form, color, input_rect)
    text_surface = font.render(user_text, True, 'black')
    form.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    blit_text(form, text, (15, 505), font)
    pygame.display.flip() 
    clock.tick(FPS)
    
    if end2:
        while start1 < end1:
            start1 = pygame.time.get_ticks()
        run = False
    elif gueses == 0:
        while start1 < end1:
            start1 = pygame.time.get_ticks()
        run = False
    

