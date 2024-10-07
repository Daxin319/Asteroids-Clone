import pygame
import config
from text import *


class Scoreboard(Text_box):

    def __init__(self, screen, font_size, color):

        super().__init__(screen, font_size, color)
        self.score = 0
        self.end_font = pygame.font.Font(None, font_size * 2)

    def increase(self, points=1):
        self.score += points

    def reset(self):
        self.score = 0

    def draw(self, screen, game_state):
        x_scale = config.SCALE_X
        y_scale = config.SCALE_Y
        
        if game_state == 0:
            score_str = f"Score: {self.score}"
            font_scale = (x_scale + y_scale) / 2
            scaled_font = pygame.font.Font(None, int(self.font.get_height() * font_scale))
            score_image = scaled_font.render(score_str, True, self.color)
            score_rect = score_image.get_rect()
            score_rect.midtop = (int(self.screen_rect.centerx * x_scale), int(10 * y_scale))
            self.screen.blit(score_image, score_rect)
        else:
            score_str = f"Final Score: {self.score}"
            font_scale = (x_scale + y_scale) / 2
            scaled_end_font_size = int(self.end_font.get_height() * font_scale)
            scaled_end_font = pygame.font.Font(None, scaled_end_font_size)
            score_image = scaled_end_font.render(score_str, True, self.color)
            score_rect = score_image.get_rect()
            vertical_pos = int(self.screen_rect.centery * y_scale) + int((self.screen_rect.height // 4) * y_scale)
            score_rect.center = (int(self.screen_rect.centerx * x_scale), vertical_pos)
            self.screen.blit(score_image, score_rect)