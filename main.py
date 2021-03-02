import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))

playerImg = pygame.image.load('pixil-frame-0.png')

PlayerX = 250
PlayerY = 250

movement_changeX = 0
movement_changeY = 0


def player(x, y):
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
            if event.key == pygame.K_RIGHT:
                movement_changeX = 0.2

            if event.key == pygame.K_UP:
                movement_changeY = -0.2
            if event.key == pygame.K_DOWN:
                movement_changeY = 0.2
        # finish of the movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement_changeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                movement_changeY = 0

        # game boundaries
        if PlayerX > 650:
            PlayerX = 650
            movement_changeX = 0
        elif PlayerX < 50:
            PlayerX = 50
            movement_changeX = 0
        if PlayerY > 450:
            PlayerY = 450
            movement_changeY = 0
        elif PlayerY < 50:
            PlayerY = 50
            movement_changeY = 0

    PlayerX += movement_changeX
    PlayerY += movement_changeY

    player(PlayerX, PlayerY)
    pygame.display.update()
