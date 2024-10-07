import pygame
from text import *

class Game_over(Text_box):

    def __init__(self, screen, font_size, color):

        super().__init__(screen, font_size, color)

        self.end_font = pygame.font.Font(None, font_size * 4)
        self.screen = screen

    def draw(self, screen, game_state):

        game_over_str = "GAME OVER"
        exit_str = "Press [Esc] to exit"

        game_over_image = self.end_font.render(game_over_str, True, (255, 0, 0))
        exit_image = self.font.render(exit_str, True, self.color)

        game_over_rect = game_over_image.get_rect()
        exit_rect = exit_image.get_rect()

        vertical_pos = self.screen_rect.centery - (self.screen_rect.height // 4)
        game_over_rect.center = (self.screen_rect.centerx, vertical_pos - 30)
        exit_rect.center = (self.screen_rect.centerx, vertical_pos + 30)
        self.screen.blit(game_over_image, game_over_rect)
        self.screen.blit(exit_image, exit_rect)