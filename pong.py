from turtledemo.nim import SCREENWIDTH

import pygame

from Ball import Ball

# pygame setup
pygame.init()
SCREENWIDTH=1280
SCREENHEIGHT=720
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
running = True

ball = Ball(SCREENWIDTH / 2, SCREENHEIGHT / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    ball.update(SCREENHEIGHT)
    ball.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()