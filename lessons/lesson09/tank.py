import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tank")
from random import randint

clock = pygame.time.Clock()
# -------- Main Program Loop -----------
done = False
STEP = 5
WHITE = (255, 255, 255)
target = [600, 300]
tank1_coord = [100, 100]
ammunition = []
KEYDOWN = set()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event)
            key = event.dict.get("key")
            KEYDOWN.add(key)
            if key == 32:
                ammunition.append([tank1_coord[0] + 33, tank1_coord[1] + 12])
        elif event.type == pygame.KEYUP:
            key = event.dict.get("key")
            if key in KEYDOWN:
                KEYDOWN.remove(key)
            # match key:
            #     case 1073741906:
            #         tank1_coord[1] -=STEP
            #     case 1073741903:
            #         tank1_coord[0] +=STEP
            #     case 1073741905:
            #         tank1_coord[1] +=STEP
            #     case 1073741904:
            #         tank1_coord[0] -=STEP
            # print(event)
    for k in KEYDOWN:
        match key:
            case 1073741906:
                tank1_coord[1] -= STEP
            case 1073741903:
                tank1_coord[0] += STEP
            case 1073741905:
                tank1_coord[1] += STEP
            case 1073741904:
                tank1_coord[0] -= STEP
            # case 32:
            #     ammunition.append([tank1_coord[0]+33, tank1_coord[1]+12])
    gameDisplay.fill(WHITE)

    target[1] += randint(-10, 10)
    for i in range(len(ammunition)):
        ammunition[i][0] += STEP * 2
        pygame.draw.circle(gameDisplay, (255, 0, 0), ammunition[i], 3, width=0)
        if (
            ammunition[i][0] < target[0] < ammunition[i][0] + 20
            and ammunition[i][1] < target[1] < ammunition[i][1] + 20
        ):
            done = True

    pygame.draw.rect(
        gameDisplay,
        (0, 0, 255),
        pygame.Rect(tank1_coord[0], tank1_coord[1], 20, 30),
        width=0,
    )
    pygame.draw.rect(
        gameDisplay,
        (0, 0, 255),
        pygame.Rect(tank1_coord[0] + 20, tank1_coord[1] + 12, 10, 5),
        width=0,
    )

    pygame.draw.rect(
        gameDisplay, (0, 255, 0), pygame.Rect(target[0], target[1], 20, 20), width=0
    )

    pygame.display.update()
    clock.tick(20)
