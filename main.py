"""
Written in python 3.6.6 and pygame 2.0.1 by Alexey Dudarev, Haileybury Almaty
Entry for FOBISIA coding competition
"""

import pygame

pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((1050, 600))

playerImgRight = pygame.image.load('New Piskel (2).png')
playerImgLeft = pygame.image.load('New Piskel-2.png.png')
currentImg = playerImgRight

floorImg = pygame.image.load('floor1.png')
rectFloor = floorImg.get_rect()
rectFloor.center = (200, 577)
rectFloor1 = floorImg.get_rect()
rectFloor1.center = (617, 577)
rectFloor2 = floorImg.get_rect()
rectFloor2.center = (1034, 577)

wallImg = pygame.image.load('Wall Sprite 1 (1).png')

rectPlayer = playerImgRight.get_rect()
rectPlayer.center = (200, 400)

movement_changeX = 0
movement_changeY = 0

# main game loop
running = True
while running:
    # background - grey
    screen.fill((142, 146, 148))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # start of the movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement_changeX = -0.5
                currentImg = playerImgLeft
            if event.key == pygame.K_RIGHT:
                movement_changeX = 1
                currentImg = playerImgRight
            if event.key == pygame.K_UP:
                movement_changeY = -1

        # finish of the movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement_changeX = 0
            if event.key == pygame.K_UP:
                movement_changeY += 2

    # game boundaries
    if rectPlayer.right > 1050:
        rectPlayer.right = 1050
        movement_changeX = 0
    elif rectPlayer.left < 0:
        rectPlayer.left = 0
        movement_changeX = 0
    if rectPlayer.bottom > 600:
        rectPlayer.bottom = 600
        movement_changeY = 0

    if rectPlayer.collidelistall([rectFloor, rectFloor1, rectFloor2]):
        movement_changeY = 0
        rectPlayer.bottom -= 1

    rectPlayer.centerx += movement_changeX
    rectPlayer.centery += movement_changeY

    screen.blit(wallImg, (-361, 338))
    screen.blit(wallImg, (50, 338))
    screen.blit(wallImg, (461, 338))
    screen.blit(wallImg, (872, 338))

    screen.blit(wallImg, (-381, 158))
    screen.blit(wallImg, (30, 158))
    screen.blit(wallImg, (441, 158))
    screen.blit(wallImg, (852, 158))

    screen.blit(floorImg, rectFloor)
    screen.blit(floorImg, rectFloor1)
    screen.blit(floorImg, rectFloor2)

    screen.blit(currentImg, rectPlayer)
    pygame.display.update()
