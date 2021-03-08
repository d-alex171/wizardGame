"""
Written in python 3.6.6 and pygame 2.0.1 by Alexey Dudarev, Haileybury Almaty
Entry for FOBISIA coding competition
"""

import pygame
from levels import set_level, rectFloor, rectFloor1, rectFloor2, rectPlatform

pygame.init()

screen = pygame.display.set_mode((1050, 600))

# creating a player model
playerImgRight = pygame.image.load('New Piskel (2).png')
playerImgLeft = pygame.image.load('New Piskel-2.png.png')
currentImg = playerImgRight
rectPlayer = playerImgRight.get_rect()
rectPlayer.center = (200, 475)

movement_changeX = 0
movement_changeY = 2

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
                movement_changeX = -3
                currentImg = playerImgLeft

            if event.key == pygame.K_RIGHT:
                movement_changeX = 3
                currentImg = playerImgRight

            if event.key == pygame.K_UP:
                movement_changeY = -3

        # finish of the movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement_changeX = 0

            if event.key == pygame.K_UP:
                movement_changeY = 2

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

    if rectPlayer.top < 2:
        rectPlayer.top = 2
        movement_changeY = 0

    # collision detection
    if rectPlayer.collidelistall([rectFloor, rectFloor1, rectFloor2]):
        movement_changeY = 0
        rectPlayer.bottom -= 1
    if rectPlayer.colliderect(rectPlatform):
        if rectPlayer.bottom >= rectPlatform.top:
            movement_changeY = 0
            rectPlayer.centery -= 2
        if rectPlayer.top <= rectPlatform.bottom:
            movement_changeY = 2
            rectPlayer.centery += 2
        if rectPlatform.right >= rectPlayer.left >= rectPlatform.centerx:
            movement_changeX = 0
            rectPlayer.centerx += 2
        if rectPlatform.left <= rectPlayer.right <= rectPlatform.centerx:
            movement_changeX = 0
            rectPlayer.centerx -= 2

    rectPlayer.centerx += movement_changeX
    rectPlayer.centery += movement_changeY

    set_level()

    # updating and project player position
    screen.blit(currentImg, rectPlayer)
    pygame.display.update()
