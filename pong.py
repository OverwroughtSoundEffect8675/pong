import pygame
import sys



pygame.init()

WIDTH , HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Pong Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 8

BALL_SIZE = 15
BALL_SPEED_X=5
BALL_SPEED_Y=5

paddle1 = pygame.Rect(50, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 60, HEIGHT/2- PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH/2 - BALL_SIZE/2, HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)


score1 = 0
score2 = 0
font = pygame.font.Font(None, 13)

clock = pygame.time.Clock()

def resetBall():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    global BALL_SPEED_X, BALL_SPEED_Y
    BALL_SPEED_X *= -1
    BALL_SPEED_Y *= -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_w] and paddle1.bottom > 0:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_w] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_w] and paddle2.bottom > 0:
        paddle2.y += PADDLE_SPEED

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    if  ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        BALL_SPEED_X *= -1




