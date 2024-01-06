import pygame.sprite
from layer import Layer

class Menu(pygame.sprite.Sprite):
    
    def __init__(self, *groups):
        self._layer = Layer.UI
        super().__init__(*groups)