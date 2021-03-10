import pygame

screen = pygame.display.set_mode((1050, 600))

# wall image loading
wallImg = pygame.image.load('sprites/Wall Sprite 1 (1).png')

# floor image loading and creating a floor object to interact with
floorImg = pygame.image.load('sprites/floor1.png')
rectFloor = floorImg.get_rect()
rectFloor1 = floorImg.get_rect()
rectFloor2 = floorImg.get_rect()
rectFloor.center = (200, 577)
rectFloor1.center = (617, 577)
rectFloor2.center = (1034, 577)

# creating platform image and platform objects to interact with  and identifying their positions
platformImg = pygame.image.load('sprites/platform1.png')
rectPlatform1 = platformImg.get_rect()
rectPlatform2 = platformImg.get_rect()
rectPlatform3 = platformImg.get_rect()
rectPlatform1.center = (-25, 250)
rectPlatform2.center = (525, 250)
rectPlatform3.center = (1075, 250)

woodenLadderIMG = pygame.image.load('sprites/wooden_ladder (2).png')
woodenPlatformIMG = pygame.image.load('sprites/wood_platform.png')

# torches animation loading
torchesAnimation = [pygame.image.load('torch animation/torch animation -1.png.png'),
                    pygame.image.load('torch animation/torch animation -2.png.png'),
                    pygame.image.load('torch animation/torch animation -3.png.png'),
                    pygame.image.load('torch animation/torch animation -4.png.png'),
                    pygame.image.load('torch animation/torch animation -5.png.png'),
                    pygame.image.load('torch animation/torch animation -6.png.png'),
                    pygame.image.load('torch animation/torch animation -7.png.png'),
                    pygame.image.load('torch animation/torch animation -8.png.png')]

playerAnimationRight = [pygame.image.load('player animation right/sprite_0.png'),
                        pygame.image.load('player animation right/sprite_1.png'),
                        pygame.image.load('player animation right/sprite_2.png'),
                        pygame.image.load('player animation right/sprite_3.png'),
                        pygame.image.load('player animation right/sprite_4.png'),
                        pygame.image.load('player animation right/sprite_5.png'),
                        pygame.image.load('player animation right/sprite_6.png'),
                        pygame.image.load('player animation right/sprite_7.png')]

playerAnimationLeft = [pygame.image.load('player animation left/sprite_0.png'),
                       pygame.image.load('player animation left/sprite_1.png'),
                       pygame.image.load('player animation left/sprite_2.png'),
                       pygame.image.load('player animation left/sprite_3.png'),
                       pygame.image.load('player animation left/sprite_4.png'),
                       pygame.image.load('player animation left/sprite_5.png'),
                       pygame.image.load('player animation left/sprite_6.png'),
                       pygame.image.load('player animation left/sprite_7.png')]

torchesCount = 0
playerCount = 0


def player_animation(direction, obj):
    global playerCount

    if direction:
        if playerCount + 1 >= 56:
            playerCount = 0
        else:
            playerCount += 1

        screen.blit(playerAnimationRight[playerCount // 7], obj)

    else:
        if playerCount + 1 >= 56:
            playerCount = 0
        else:
            playerCount += 1

        screen.blit(playerAnimationLeft[playerCount // 7], obj)


def torches_animation():
    global torchesCount

    if torchesCount + 1 >= 32:
        torchesCount = 0
    else:
        torchesCount += 1

    screen.blit(torchesAnimation[torchesCount // 4], (50, 338))
    screen.blit(torchesAnimation[torchesCount // 4], (380, 338))
    screen.blit(torchesAnimation[torchesCount // 4], (610, 338))
    screen.blit(torchesAnimation[torchesCount // 4], (930, 338))


def set_level():
    # projecting every wall sprite
    screen.blit(wallImg, (-350, 338))
    screen.blit(wallImg, (50, 338))
    screen.blit(wallImg, (461, 338))
    screen.blit(wallImg, (872, 338))

    screen.blit(wallImg, (-381, 122))
    screen.blit(wallImg, (30, 122))
    screen.blit(wallImg, (441, 122))
    screen.blit(wallImg, (852, 122))

    screen.blit(wallImg, (-381, -94))
    screen.blit(wallImg, (30, -94))
    screen.blit(wallImg, (441, -94))
    screen.blit(wallImg, (852, -94))

    # projecting every floor sprite
    screen.blit(floorImg, rectFloor)
    screen.blit(floorImg, rectFloor1)
    screen.blit(floorImg, rectFloor2)

    screen.blit(woodenLadderIMG, (125, 39))
    screen.blit(woodenLadderIMG, (677, 39))

    screen.blit(woodenPlatformIMG, (650, 202))
    screen.blit(woodenPlatformIMG, (50, 202))

    screen.blit(platformImg, rectPlatform1)
    screen.blit(platformImg, rectPlatform2)
    screen.blit(platformImg, rectPlatform3)
