import pygame

screen = pygame.display.set_mode((1050, 600))

# wall image loading
wallImg = pygame.image.load('Wall Sprite 1 (1).png')

# floor image loading and creating a floor object to interact with
floorImg = pygame.image.load('floor1.png')
rectFloor = floorImg.get_rect()
rectFloor1 = floorImg.get_rect()
rectFloor2 = floorImg.get_rect()
rectFloor.center = (200, 577)
rectFloor1.center = (617, 577)
rectFloor2.center = (1034, 577)

platformImg = pygame.image.load('platform1.png')
rectPlatform = platformImg.get_rect()
rectPlatform.center = (500, 250)

"""
# torches animation loading
torchesAnimation = [pygame.image.load('torch animation/torch animation -1.png.png'),
                    pygame.image.load('torch animation/torch animation -2.png.png'),
                    pygame.image.load('torch animation/torch animation -3.png.png'),
                    pygame.image.load('torch animation/torch animation -4.png.png'),
                    pygame.image.load('torch animation/torch animation -5.png.png'),
                    pygame.image.load('torch animation/torch animation -6.png.png'),
                    pygame.image.load('torch animation/torch animation -7.png.png'),
                    pygame.image.load('torch animation/torch animation -8.png.png')]
"""


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

    screen.blit(platformImg, rectPlatform)


