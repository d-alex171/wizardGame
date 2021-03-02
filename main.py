import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))

playerImgRight = pygame.image.load('New Piskel (2).png')
playerImgleft = pygame.image.load('New Piskel-2.png.png')
currentImg = playerImgRight

PlayerX = 250
PlayerY = 300

movement_changeX = 0
movement_changeY = 0


def player(playerImg, x, y):
    screen.blit(playerImg, (x, y))


# main game loop
running = True
while running:
    # background - black
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # start of the movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement_changeX = -0.2
                currentImg = playerImgleft
            if event.key == pygame.K_RIGHT:
                movement_changeX = 0.2
                currentImg = playerImgRight
            if event.key == pygame.K_UP:
                movement_changeY = -0.2

        # finish of the movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement_changeX = 0
            if event.key == pygame.K_UP:
                movement_changeY = 0.15

    # game boundaries
    if PlayerX > 600:
        PlayerX = 600
        movement_changeX = 0
    elif PlayerX < 0:
        PlayerX = 0
        movement_changeX = 0
    if PlayerY > 300:
        PlayerY = 300
        movement_changeY = 0

    PlayerX += movement_changeX
    PlayerY += movement_changeY

    player(currentImg, PlayerX, PlayerY)
    pygame.display.update()
