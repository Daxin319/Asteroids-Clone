import pygame


class Scoreboard(pygame.sprite.Sprite):

    def __init__(self, screen, font_size=36, color=(255, 255, 255)):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = color

    def increase(self, points=1):
        self.score += points

    def reset(self):
        self.score = 0

    def draw(self, screen):
        score_str = f"Score: {self.score}"
        score_image = self.font.render(score_str, True, self.color)
        score_rect = score_image.get_rect()
        score_rect.midtop = (self.screen_rect.centerx, 10)
        self.screen.blit(score_image, score_rect)