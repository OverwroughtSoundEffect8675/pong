import pygame, random

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xvel= random.randint(-10,10)
        self.yvel= random.randint(-10,10)
    def update(self, screenHeight):
        self.x+=self.xvel
        self.y+=self.yvel
        if self.y <= 0:
            self.yvel = -self.yvel
        if self.y >= screenHeight:
            self.yvel = -self.yvel
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 10)