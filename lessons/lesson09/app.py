import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My first game tank') 

COLORs = [ ( 0, 255, 255)
 ,( 0, 0, 0)
, ( 0, 0, 255)
, (255, 0, 255)
, (128, 128, 128)
, ( 0, 128, 0)
, ( 0, 255, 0)
, (128, 0, 0)
, ( 0, 0, 128)
, (128, 128, 0)
, (128, 0, 128)
, (255, 0, 0)
, (192, 192, 192)
, ( 0, 128, 128)
, (255, 255, 255)
, (255, 255, 0)  
]

font = pygame.font.SysFont('Calibri', 25, True, False)

WHITE = (255, 255, 255)
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------

POINTS = []
while not done:
    
    for event in pygame.event.get(): 
        # print(event)
        if event.type == pygame.QUIT:
            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            data = event.dict
            if data["button"] == 1:
                POINTS.append(data["pos"])
            elif data["button"] == 3:
                if POINTS:
                    POINTS.pop()

    gameDisplay.fill(WHITE)
    if len(POINTS) > 3:
        pygame.draw.polygon(gameDisplay, COLORs[len(POINTS)%len(COLORs)], POINTS, width=0)
    for point in POINTS:
        text = font.render( f"{point}",True,COLORs[1])
        gameDisplay.blit(text, [point[0]-50, point[1]-20])

    pygame.display.update()
    clock.tick(60)

