import pygame
import config
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius, group):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shots = group
        self.cd = 0

    def triangle(self):
        scaled_radius = self.radius * min(config.SCALE_X, config.SCALE_Y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * scaled_radius / 1.5
        scaled_position = pygame.Vector2(self.position.x * config.SCALE_X, self.position.y * config.SCALE_Y)
        a = scaled_position + forward * scaled_radius
        b = scaled_position - forward * scaled_radius - right
        c = scaled_position - forward * scaled_radius + right
        return [a, b, c]
    
    def draw(self, screen, game_state):
        pygame.draw.polygon(screen, "green", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cd -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()


    def shoot(self):
        if self.cd > 0:
            pass
        else:
            self.cd = SHOT_CD
            shot = Shot(self.position, SHOT_RADIUS)
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = direction * SHOT_SPEED
            self.shots.add(shot)