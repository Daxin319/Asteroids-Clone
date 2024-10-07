import pygame
import config
from constants import *
from circleshape import *

class Shot(CircleShape):

    def __init__(self, position, radius):
        super().__init__(position.x, position.y, radius)

    def draw(self, screen, game_state):
        scaled_radius = self.radius * min(config.SCALE_X, config.SCALE_Y)
        scaled_position = (self.position.x * config.SCALE_X, self.position.y * config.SCALE_Y)
        pygame.draw.circle(screen, "red", scaled_position, scaled_radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt