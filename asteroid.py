import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, dt):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split1 = self.velocity.rotate(random_angle)
            split2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = split1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = split2 * 1.2
