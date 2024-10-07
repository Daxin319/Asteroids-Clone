#base class for text boxes

import pygame

class Text_box(pygame.sprite.Sprite):

    def __init__(self, screen, font_size=36, color=(255, 255, 255), game_state = None):
    
        if hasattr(self, "containers"):
                super().__init__(self.containers)
        else:
                super().__init__()
            
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.Font(None, font_size)
        self.color = color

    def draw(self, screen, game_state = None):
          pass
    