import pygame.sprite
import assets
import configs
from layers import Layers

class Background(pygame.sprite.Sprite):
    """ Background sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, index, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
        
    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH