import pygame
from enums.layers import Layers

class Slider(pygame.sprite.Sprite):
    """ Slider sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.pos = pos
        self.size = size
        self.slider_left_pos = pos[0] - (size[0] // 2)
        self.slider_right_pos = pos[0] + (size[0] // 2)
        self.slider_top_pos = pos[1] - (size[1] // 2)
        self.min = min
        self.max = max
        self.handle_width = 10
        self.active = False
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val #percentage
        self.image = pygame.Surface([size[0], size[1]])
        self.rect = self.image.get_rect(topleft=(self.slider_left_pos, self.slider_top_pos))
        self.container_rect = pygame.Rect(0, 0, size[0], size[1])
        self.handle_rect = pygame.Rect(self.initial_val, 0, self.handle_width, size[1])
        
    def update(self, dt):
        pygame.draw.rect(self.image, pygame.color.Color("darkgray"), self.container_rect)
        if self.active:
            pygame.draw.rect(self.image, pygame.color.Color("#6110a2"), self.handle_rect)
        else:
            pygame.draw.rect(self.image, pygame.color.Color("black"), self.handle_rect)
        
    def move_slider(self, mouse_pos):
        """ Move slider from mouse position

        Args:
            mouse_pos (_type_): int
        """
        self.handle_rect.centerx = mouse_pos[0] - self.slider_left_pos
    
    def set_slider(self, value):
        """ Move slider from value

        Args:
            value (_type_): int
        """
        self.handle_rect.centerx = self.handle_rect.centerx + value
        
    def get_value(self):
        """ Get slider value

        Returns:
            _type_: float
        """
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.handle_rect.centerx
        return (button_val / val_range) * (self.max-self.min) + self.min
    
    