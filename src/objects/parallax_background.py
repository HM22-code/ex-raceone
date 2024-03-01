import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class ParallaxBackground(pygame.sprite.Sprite):
    """ ParallaxBackground sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, index: int, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.index = index
        self.image = utils.assets.get_sprite("parallax-1.png")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * self.index, 0))
    
    