import pygame.sprite
import assets
import configs
from enums.layers import Layers

class Title(pygame.sprite.Sprite):
    """ Title sprite class

    Args:
        pygame (_type_): sprite
    """
    
    SCALE = 3
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = assets.get_sprite("title")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.SCALE), int(self.image.get_height() * self.SCALE)))
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 6))