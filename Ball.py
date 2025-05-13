import pygame, random, math

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        direction = random.randint(0,360)
        self.xvel= 6 * math.cos(math.radians(direction))
        self.yvel= 6 * math.sin(math.radians(direction))
    def update(self, screenHeight):
        self.x+=self.xvel
        self.y+=self.yvel
        if self.y <= 0:
            self.yvel = -self.yvel
        if self.y >= screenHeight:
            self.yvel = -self.yvel
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 10)