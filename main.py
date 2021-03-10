"""
Written in python 3.6.6 and pygame 2.0.1 by Alexey Dudarev, Haileybury Almaty
Entry for FOBISIA coding competition
"""

import pygame
from levels import *

pygame.init()
# setting some information about the window
screen = pygame.display.set_mode((1050, 600))
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Magic Castle')

# creating a player model
playerImgRight = pygame.image.load('player animation right/sprite_0.png')
playerImgLeft = pygame.image.load('player animation left/sprite_0.png')
currentImg = playerImgRight
rectPlayer = playerImgRight.get_rect()
rectPlayer.center = (200, 450)

movement_changeX = 0
movement_changeY = 2
direction = True

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
                direction = False

            if event.key == pygame.K_RIGHT:
                movement_changeX = 3
                currentImg = playerImgRight
                direction = True

            if event.key == pygame.K_UP:
                movement_changeY = -5

        # finish of the movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement_changeX = 0

            if event.key == pygame.K_UP:
                movement_changeY = 4

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
    elif rectPlayer.colliderect(rectPlatform2):
        if rectPlatform2.left <= rectPlayer.right <= rectPlatform2.centerx:
            movement_changeX = 0
            rectPlayer.centerx -= 2
        elif rectPlatform2.centerx <= rectPlayer.left <= rectPlatform2.right:
            movement_changeX = 0
            rectPlayer.centerx += 2

        if rectPlatform2.top <= rectPlayer.bottom <= rectPlatform2.centery:
            movement_changeY = 0
            rectPlayer.centery -= 2

        elif rectPlatform2.centery <= rectPlayer.top <= rectPlatform2.bottom:
            movement_changeY = 2
            rectPlayer.centery += 2
    elif rectPlayer.colliderect(rectPlatform1):
        if rectPlatform1.left <= rectPlayer.right <= rectPlatform1.centerx:
            movement_changeX = 0
            rectPlayer.centerx -= 2
        elif rectPlatform1.centerx <= rectPlayer.left <= rectPlatform1.right:
            movement_changeX = 0
            rectPlayer.centerx += 2

        if rectPlatform1.top <= rectPlayer.bottom <= rectPlatform1.centery:
            movement_changeY = 0
            rectPlayer.centery -= 2

        elif rectPlatform1.centery <= rectPlayer.top <= rectPlatform1.bottom:
            movement_changeY = 2
            rectPlayer.centery += 2
    elif rectPlayer.colliderect(rectPlatform3):
        if rectPlatform3.left <= rectPlayer.right <= rectPlatform3.centerx:
            movement_changeX = 0
            rectPlayer.centerx -= 2
        elif rectPlatform3.centerx <= rectPlayer.left <= rectPlatform3.right:
            movement_changeX = 0
            rectPlayer.centerx += 2

        if rectPlatform3.top <= rectPlayer.bottom <= rectPlatform3.centery:
            movement_changeY = 0
            rectPlayer.centery -= 2

        elif rectPlatform3.centery <= rectPlayer.top <= rectPlatform3.bottom:
            movement_changeY = 2
            rectPlayer.centery += 2

    rectPlayer.centerx += movement_changeX
    rectPlayer.centery += movement_changeY

    set_level()
    torches_animation()
    # updating and project player position
    if movement_changeX != 0:
        player_animation(direction, rectPlayer)
    else:
        screen.blit(currentImg, rectPlayer)

    pygame.display.update()
