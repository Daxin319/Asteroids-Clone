import pygame
from text import *


class Scoreboard(Text_box):

    def __init__(self, screen, font_size, color):

        super().__init__(screen, font_size, color)
        self.score = 0

    def increase(self, points=1):
        self.score += points

    def reset(self):
        self.score = 0

    def draw(self, screen, game_state):
        
        if game_state == 0:
            score_str = f"Score: {self.score}"
            score_image = self.font.render(score_str, True, self.color)
            score_rect = score_image.get_rect()
            score_rect.midtop = (self.screen_rect.centerx, 10)
            self.screen.blit(score_image, score_rect)
        else:
            score_str = f"Final Score: {self.score}"
            score_image = self.font.render(score_str, True, self.color)
            score_rect = score_image.get_rect()
            score_rect.midbottom = (self.screen_rect.centerx, -100)
            self.screen.blit(score_image, score_rect)