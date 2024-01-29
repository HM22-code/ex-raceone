import pygame.sprite
import assets
import configs
from layers import Layers

class Title(pygame.sprite.Sprite):
    """ Title sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = assets.get_sprite("title")
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 6))