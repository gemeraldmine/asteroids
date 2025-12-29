import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

def Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, radius):
        pygame.draw.circle(screen, "white", self.(x, y), self.radius, LINE_WIDTH)

    def update(self, )
