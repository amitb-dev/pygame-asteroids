import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        

        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast1.velocity = vel1 * 1.2
        ast2.velocity = vel2 * 1.2

    def get_score(self):
        # Determine score based on radius
        if self.radius > ASTEROID_MIN_RADIUS * 2:
            return SCORE_LARGE_ASTEROID
        elif self.radius > ASTEROID_MIN_RADIUS:
            return SCORE_MEDIUM_ASTEROID
        else:
            return SCORE_SMALL_ASTEROID