import pygame
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 100
    def update(self):
        pass
    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.x, self.y, self.width, self.height))