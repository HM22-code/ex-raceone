import pygame.sprite
import assets
import configs.screen
from enums.layers import Layers

class Floor(pygame.sprite.Sprite):
    """ Floor sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, index, *groups):
        super().__init__(*groups)
        self._layer = Layers.FLOOR
        self.image = assets.get_sprite("floor")
        self.rect = self.image.get_rect(bottomleft=(configs.screen.SCREEN_WIDTH * index, configs.screen.SCREEN_HEIGHT))
        
    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.x = configs.screen.SCREEN_WIDTH