import pygame

# Base class for game objects:
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # will return to this
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen, game_state = None):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, object):
        distance = self.position.distance_to(object.position)
        return distance <= self.radius + object.radius