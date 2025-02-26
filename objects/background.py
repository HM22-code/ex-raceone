import pygame.sprite
import utils.assets
from enums.layers import Layers

class Background(pygame.sprite.Sprite):
    """ Background sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = utils.assets.get_sprite("background.png")
        self.rect = self.image.get_rect(topleft=(0, 0))