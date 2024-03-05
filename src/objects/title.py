import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class Title(pygame.sprite.Sprite):
    """ Title sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = utils.assets.get_sprite("title.png")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 1), int(self.image.get_height() * 1)))
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 6))