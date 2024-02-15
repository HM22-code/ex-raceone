import pygame.sprite
import assets
import configs
from enums.layers import Layers

class Background(pygame.sprite.Sprite):
    """ Background sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(0, 0))