import pygame
import config
import random
from constants import *
from circleshape import *
from scoreboard import *

class Asteroid(CircleShape):
    scores = {60:5, 40:10, 20:20}

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.score_value = self.scores[self.radius]

    def draw(self, screen, game_state):
        scaled_radius = self.radius * min(config.SCALE_X, config.SCALE_Y)
        scaled_position = (self.position.x * config.SCALE_X, self.position.y * config.SCALE_Y)
        pygame.draw.circle(screen, "white", scaled_position, scaled_radius, 2)

    def update(self, dt):
        movement = self.velocity * dt
        self.position += movement

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_vector1 * 1.2
            new_asteroid2.velocity = new_vector2 * 1.2
            return new_asteroid1, new_asteroid2