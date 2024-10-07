import pygame
import config
from text import *

class Game_over(Text_box):

    def __init__(self, screen, font_size, color):

        super().__init__(screen, font_size, color)

        self.end_font = pygame.font.Font(None, font_size * 4)
        self.screen = screen

    def draw(self, screen, game_state):
        x_scale = config.SCALE_X
        y_scale = config.SCALE_Y

        game_over_str = "GAME OVER"
        exit_str = "Press [Esc] to exit"
        
        scaled_end_font = pygame.font.Font(None, int(self.end_font.get_height() * (x_scale + y_scale) / 2))
        scaled_font = pygame.font.Font(None, int(self.font.get_height() * (x_scale + y_scale) / 2))
        game_over_image = scaled_end_font.render(game_over_str, True, (255, 0, 0))
        exit_image = scaled_font.render(exit_str, True, self.color)
        game_over_rect = game_over_image.get_rect()
        exit_rect = exit_image.get_rect()

        vertical_pos = int(self.screen_rect.centery * y_scale - (self.screen_rect.height // 4) * y_scale)
        game_over_rect.center = (int(self.screen_rect.centerx * x_scale), int(vertical_pos - 30 * y_scale))
        exit_rect.center = (int(self.screen_rect.centerx * x_scale), int(vertical_pos + 30 * y_scale))
    
        self.screen.blit(game_over_image, game_over_rect)
        self.screen.blit(exit_image, exit_rect)