import pygame
from enums.layers import Layers

class Slider(pygame.sprite.Sprite):
    
    HANDLE_WIDTH = 10
    
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
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val #percentage
        self.image = pygame.Surface([size[0], size[1]])
        self.rect = self.image.get_rect(topleft=(self.slider_left_pos, self.slider_top_pos))
        self.container_rect = pygame.Rect(0, 0, size[0], size[1])
        self.handle_rect = pygame.Rect(self.initial_val, 0, self.HANDLE_WIDTH, size[1])
        
    def update(self):
        pygame.draw.rect(self.image, "darkgray", self.container_rect)
        pygame.draw.rect(self.image, "black", self.handle_rect)
        
    def move_slider(self, mouse_pos):
        self.handle_rect.centerx = mouse_pos[0] - self.slider_left_pos
        
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.handle_rect.centerx
        return (button_val / val_range) * (self.max-self.min) + self.min
    
    